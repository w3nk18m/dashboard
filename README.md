# reflex-website

## Setup Locally

1. Navigate to the project directory.

    ```bash
    cd dashboard
    ```

2. Create a virtual environment.

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment.

    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies.

    ```bash
    python -m pip install -r requirements.txt
    ```

5. Initialize the reflex project.

    ```bash
    reflex init
    ```

6. Run the project.

    ```bash
    reflex run --env prod
    ```

    *Open the browser and go to `http://localhost:3000/` to see the website.*
