<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <h1 style="text-align: center;">CarScanner - Vehicle Information System</h1>
    <p>
        <strong>CarScanner</strong> is a dynamic software tool built for users in Israel, allowing for comprehensive vehicle information searches based on a license plate number. It combines user-friendly design with practical functionality, making it easy to retrieve essential car details.
    </p>
    <h2>Features</h2>
    <p>The software includes a variety of features designed to simplify car searches and provide a seamless user experience:</p>
    <ul>
        <li><strong>License Plate Lookup:</strong> Enter a license plate number to retrieve detailed car information, such as the car's model, make, year, and additional technical details.</li>
        <li><strong>Ownership History:</strong> View a concise history of the vehicle, including the number of previous owners and significant milestones.</li>
        <li><strong>Mileage Records:</strong> Display the most up-to-date mileage of the car based on its last reported test (e.g., annual roadworthiness inspections).</li>
        <li><strong>Vehicle Images:</strong> In some cases, the app displays images of the car from previous sales or other records.</li>
        <li><strong>WhatsApp Integration:</strong> Send the retrieved car details directly via WhatsApp to other users for easy sharing.</li>
        <li><strong>Search History:</strong> The app stores the last 5 searches for quick access to previous results.</li>
        <li><strong>Image Viewer:</strong> Use an integrated image slider to view available images of the car, with smooth navigation between images.</li>
    </ul>
    <h2>How it Works</h2>
    <p>The application uses a simple and intuitive graphical user interface (GUI) built with Python's Tkinter library. Here's a breakdown of the process:</p>
    <ol>
        <li>Users input a license plate number into the application.</li>
        <li>The system retrieves data from a pre-defined source (e.g., an API or dataset).</li>
        <li>The retrieved data is displayed in a visually appealing format, showing essential details about the car.</li>
        <li>If applicable, the app fetches relevant car images and displays them using an image slider.</li>
        <li>Users can share the details via WhatsApp with a single click, making it easy to communicate with potential buyers, friends, or family.</li>
        <li>The last five searches are stored and can be accessed through the "History" section of the app.</li>
        </ol>
    <h2>Unique Functionalities</h2>
    <p>CarScanner includes several standout features that enhance its usability:</p>
    <ul>
        <li><strong>Localized Design:</strong> The application is tailored specifically for the Israeli market, ensuring compatibility with local data sources and user needs.</li>
        <li><strong>Data Safety:</strong> All user queries are processed locally (if no external API is used), ensuring privacy and security.</li>
        <li><strong>Modern Aesthetics:</strong> The application features a clean, modern design with easy navigation and dark mode styling.</li>
        <li><strong>Error Handling:</strong> The app includes comprehensive error handling to manage invalid license plate entries or missing data gracefully.</li>
    </ul>
    <h2>System Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Tkinter (usually included with Python installation)</li>
        <li>Additional Libraries: <code>Pillow</code> (for image processing, if required), <code>requests</code> (if APIs are used)</li>
    </ul>
    <h2>How to Run the Application</h2>
    <ol>
        <li>Ensure that you have Python 3 installed on your computer.</li>
        <li>Download all the files from the GitHub repository (or use <code>git clone</code>).</li>
        <li>Run the <code>Design.py</code> file to start the application:</li>
        <pre><code>python Design.py</code></pre>
    </ol>
    <h2>Project Structure</h2>
    <p>The project contains the following files and directories:</p>
    <ul>
        <li><strong>Design.py:</strong> Contains the main graphical user interface and manages the overall application layout.</li>
        <li><strong>ButtonManager.py:</strong> Handles button clicks and application logic, such as searching for car details and sending WhatsApp messages.</li>
        <li><strong>ImageSlider.py:</strong> Manages the image viewer and slider functionality for car images.</li>
        <li><strong>History.py:</strong> Implements the "Search History" feature, allowing users to view and select from previous searches.</li>
        <li><strong>assets/:</strong> Includes images, such as background designs and button icons, used throughout the application.</li>
        <li><strong>History.txt:</strong> A local file used to store the last five searches made by the user.</li>
    </ul>
    <h2>How to Contribute</h2>
    <p>If you want to contribute to the project, here are some areas for improvement:</p>
    <ul>
        <li>Adding additional API integrations for more comprehensive car data.</li>
        <li>Enhancing the user interface for a more polished look.</li>
        <li>Extending the history feature to allow more searches or cloud-based storage.</li>
        <li>Improving the image slider functionality.</li>
        <li>Translating the app into multiple languages.</li>
    </ul>
    <h2>Screenshot</h2>
    <p>Here is a screenshot of the application in action:</p>
    <img src="https://i.postimg.cc/zDP5r2WW/image.png" alt="CarScanner Image" style="max-width:50%; height:auto; border: 1px solid #ddd; border-radius: 5px;">

</body>
</html>
