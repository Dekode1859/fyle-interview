import json
from flask import Blueprint, jsonify, make_response
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum, GradeEnum
from .schema import AssignmentSchema, AssignmentSubmitSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principal_assignments = Assignment.get_assignments_by_principal()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    assignment = Assignment.get_by_id(grade_assignment_payload.id)
    print(assignment.state)
    if assignment.state == AssignmentStateEnum.DRAFT and assignment.teacher_id is None:
        return make_response(jsonify({'error': 'Cannot grade a draft assignment'}), 400)
    else:
        assignment.grade = grade_assignment_payload.grade
        assignment.state = AssignmentStateEnum.GRADED
        db.session.commit()
        return APIResponse.respond(data=AssignmentSchema().dump(assignment))