

# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app


# Copy your code
COPY users.py .


# Run the program
CMD ["python","users.py"]



# RUN IN TERMINAL :
# docker buildx build --load -t mod8_ex4:1.0.0 .

# to save my image:
# docker save mod8_ex4:1.0.0 -o mod8_ex4.tar