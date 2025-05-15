# Use an official OpenJDK runtime as the base image
FROM openjdk:17

# Set the working directory inside the container
WORKDIR /app

# Copy the Java file into the container
COPY PalindromeChecker.java .

# Compile the Java file
RUN javac PalindromeChecker.java

# Set the command to run the compiled Java program
CMD ["java", "PalindromeChecker"]
