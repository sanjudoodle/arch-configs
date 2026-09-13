# Install LOCALSTACK (NO LOGIN)

```bash
# pull the localstack image
podman pull "docker.io/localstack/localstack:4.14.0"

# create container
podman run --name localstack -p 127.0.0.1:4566:4566 -p 127.0.0.1:4510-4559:4510-4559 -d docker.io/localstack/localstack:4.14.0

# install aws-cli-v2
sudo pacman -S --needed aws-cli-v2

# setup a fake credentials profile
aws configure
# "test" for both access tokens
# "eu-north-1" region
# "json" format

# assign http://127.0.0.1:4566 to AWS_ENDPOINT_URL env variable
export AWS_ENDPOINT_URL="http://127.0.0.1:4566"
