## Installation
1. Clone this repository
   ```
   git clone <git-repo-link>
   ```
3. cd into the directory of the cloned repo
   ```
   cd <local-repo-name>
   ```
4. make sure you hae Docker Desktop installed with the CLI then you can run this command
   ```
   docker build . --tag <build-name>
   ```
6. once the build is finished run a container<br>
   ```
   docker run -p 8080:7755 <build-name>
   ```
7. if everything goes well you can go to:<br>
   ```
   localhost:8080
   ```
   <br>
   on your browser

