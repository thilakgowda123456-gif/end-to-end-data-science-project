# end-to-end-data-science-project

company name : codetech It solutions

Name : Thilakgowda BK

domain name : data science

Intern ID : CTIS6902

Duration : 4 weeks

Description of the task :

This task focuses on deploying a machine learning model as a web API using Flask. The main objective is to make a trained model accessible over the internet (or locally) so that users or applications can send input data and receive predictions in real time. This is an important step in moving from a trained model to a practical, usable system.

The process begins by importing the required libraries. Flask is used to create the web server and define API endpoints. The request module helps receive incoming data from users, while jsonify is used to send responses in JSON format. NumPy is used for handling numerical data, and joblib is used to load the previously saved machine learning model and scaler.

The Flask application is initialized, and the trained model (model.pkl) along with the scaler (scaler.pkl) are loaded from storage. These files were created in a previous task during the model training phase. Loading them here avoids retraining the model every time the application runs, making the system efficient and production-ready.

The application defines two main routes (endpoints). The first route, "/", is a simple home route that returns a message indicating that the API is running. This is useful for testing whether the server is active.

The second route, "/predict", is the core functionality of the API. It is designed to accept POST requests, meaning users must send data to this endpoint in JSON format. The input data is expected to include features such as "age" and "salary", which are the same features used to train the model.

Inside the prediction function, the incoming JSON data is extracted using request.get_json(). The features are then arranged into a NumPy array and reshaped into the correct format expected by the model. Since the model was trained on scaled data, the same scaler is applied to the input features to ensure consistency.

After preprocessing, the model makes a prediction using the predict() method. The result is typically a class label (for example, 0 or 1 indicating whether a purchase is predicted or not). The prediction is then converted into a standard Python integer and returned as a JSON response. This allows other applications, such as web or mobile apps, to easily consume the output.

Finally, the application is run in debug mode, which is useful during development because it provides detailed error messages and automatically reloads the server when changes are made.

Overall, this task demonstrates how to take a trained machine learning model and deploy it as a RESTful API. It connects the model to real-world usage, enabling external systems to interact with it. This approach is widely used in production environments where machine learning models need to provide predictions dynamically, such as in recommendation systems, fraud detection, or customer behavior prediction.

give the descrpition of about 500 words

This task involves creating a web-based application programming interface (API) to serve a trained machine learning model using the Flask framework. The purpose of this task is to bridge the gap between model development and real-world usage by allowing external users or systems to interact with the model through HTTP requests. Instead of running predictions manually in a script, the model can now provide results dynamically in response to user input.

The process begins by importing the required libraries. Flask is used to build the web server and define routes that handle incoming requests. The request module is responsible for receiving input data from users, while jsonify helps format the output into JSON, which is a standard format for web communication. NumPy is used for numerical operations, and joblib is used to load the pre-trained machine learning model and scaler from saved files.

The application is initialized using Flask, and the trained model (model.pkl) along with the scaler (scaler.pkl) are loaded into memory. These files were created during the training phase and contain the learned patterns and preprocessing logic. Loading them at runtime ensures that predictions can be made quickly without retraining the model, making the system efficient and suitable for deployment.

The API defines two main routes. The root route ("/") acts as a basic health check and returns a simple message indicating that the API is running. This is useful for verifying that the server is active and functioning properly.

The main functionality is implemented in the "/predict" route, which accepts POST requests. This route is designed to receive input data in JSON format, typically containing features such as age and salary. These features must match the format and order used during model training. Once a request is received, the data is extracted and converted into a NumPy array. The array is reshaped to match the input requirements of the model.

Before making predictions, the input data is passed through the same scaler used during training. This step is critical because machine learning models perform best when the input data is processed in the same way as the training data. After scaling, the processed features are fed into the model to generate a prediction.

The model outputs a result, usually a binary value indicating a class (for example, whether a customer is likely to make a purchase). This result is then converted into a standard Python data type and returned as a JSON response. This makes it easy for other applications, such as web frontends or mobile apps, to consume and display the prediction.

Finally, the Flask application is run in debug mode, which is helpful during development as it provides detailed error messages and automatically reloads the server when changes are made.

Overall, this task demonstrates how to deploy a machine learning model as a RESTful API, enabling real-time predictions and integration with other systems. It is a crucial step in making machine learning solutions practical, scalable, and accessible in real-world applications.

output of the task:

