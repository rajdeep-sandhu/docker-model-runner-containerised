# Basic Docker Model Runner Streamlit LLM Chat Interface

Based on [The Easiest Ways to Run LLMs Locally - Docker Model Runner Tutorial](https://www.youtube.com/watch?v=GOgfQxDPaDw).

## Files

- `main.py`
  - This uses a `streamlit` interface and `openai` to interact with the Docker Model Runner, which needs to be running on the local machine.
  - `API_KEY` uses a dummy value, as required by the `openai` API, but is not needed for a local LLM.
- `backend.env`
  - `BASE_URL=http://host.docker.internal:12434/engines/llama.cpp/v1/`: This URL tells Docker to interact with the Docker Model Runner on the local machine instead of looking for the service in a different container.
  - `API_KEY`: Dummy value.
- `docker-compose.yml`: Sets up the required services.
  - `app`: `streamlit` uses port `8501`. The service depends on the `llm` service to be able to communicate with the Docker Model Runner.
  - `llm`: The syntax makes `LLM_MODEL_NAME` default to `ai/smollm3` if not set in the environment or present in the `backend.env`. See [Use AI Models in Compose](https://docs.docker.com/ai/compose/models-and-compose/).
- `Dockerfile`

## To Run

- Clone the repo.
- Ensure Docker Desktop is running.
- In the root folder:
  
  ```bash
  docker compose build

  # Run the app
  docker compose up
  ```

- Open [http://localhost:8501](http://localhost:8501) in the browser.
- When finished, open a separate terminal.
  
  ```bash
  docker compose down
  ```
