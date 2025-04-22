# AI Safety Glossary

## Development

### Developing with Docker

Create a Docker container with a Python environment and the required dependencies. This is useful when developers are working on machines with different operating systems or configurations.

```
docker-compose up ai-safety-develop --build
```

In a separate terminal, open a bash shell in the container:

```
docker exec -it ai-safety-develop /bin/bash
```
