# didydoc


# Didydoc: Online Library and Discussion Platform

Didydoc is an online platform designed to serve as both a digital library and a discussion forum. Users can upload, manage, and classify digital documents while engaging in discussions on various topics through an integrated blog feature.

## Key Features

- **User Authentication**: Users can securely create accounts and log into the Didydoc platform.
  
- **Document Management**: Didydoc allows users to upload digital documents in multiple formats such as PDF, DOCX, TXT, etc., and provides tools for managing and organizing their library.
  
- **Automatic Document Classification**: Leveraging a specially developed Machine Learning model, Didydoc automatically categorizes uploaded documents based on their content.
  
- **Integrated Blog**: Didydoc features a built-in blog where users can post messages, initiate discussions on different topics, and interact with other users through comments.

## Technologies Used

- **Flask (Python)**: A lightweight web framework used for backend development.
  
- **HTML/CSS/JavaScript**: Standard web development languages utilized for crafting the user interface.
  
- **SQLite**: A relational database management system employed for storing user information, document data, blog posts, etc.

## Prerequisites

- Python 3.x installed on your system.
  
- Required dependencies are listed in the `requirements.txt` file and can be installed via `pip`.

## Installation and Configuration

1. Clone this repository to your local machine.
  
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables in the `.env` file
4. Initialize the database by running the following commands:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Launch the application by running the following command:
   ```
   python app.py
   ```

Didydoc will then be accessible at `http://127.0.0.1:5000`.

## Contributing

Contributions to this project are welcome! To propose improvements, bug fixes, or new features, please submit a pull request following the guidelines in the `CONTRIBUTING.md` file.

## Authors

- [BOCAQUELON Eddy Juveno](https://github.com/juven0) - Lead Developer


