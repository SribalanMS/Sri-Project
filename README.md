# Sri-Project  

**To monitor a folder** for new files and move them to another folder using Python, you can use the following modules:

**os**: Provides functions for interacting with the operating system, like listing directory contents.
**logging**: Allows you to record events and errors during execution for easier debugging and monitoring.
**shutil**: Offers high-level operations on files and collections of files, like moving them between directories.
**time**: Enables you to control the timing of actions within your script.

Steps involved:

Set up Logging: Configure logging to track the movement of files and any errors encountered.

Define Source and Destination: Specify the paths of the folders where files are monitored (source) and where files should be moved (destination).

Monitor and Move Files: Continuously check the source folder for new files. When files are found, move each file to the destination folder using shutil.move.

Error Handling: Implement error handling to manage cases where files cannot be moved.

This approach ensures automated file management, useful for tasks like data processing or automated file transfers between directories.
