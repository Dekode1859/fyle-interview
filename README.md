## How to run Docker
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
   on your browser<br>
8. you should see this message on the webpage:<br>
   ![image](https://github.com/Dekode1859/fyle-interview/assets/93965493/ce7432ee-d203-4e4a-9067-b59866cbb347)


