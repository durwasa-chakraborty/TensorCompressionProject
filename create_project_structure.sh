# Bash script to create the project directory structure
#!/bin/bash

# Base project directory
PROJECT_DIR="TensorCompressionProject"

# Create base directory
mkdir -p $PROJECT_DIR

# Create subdirectories
mkdir -p $PROJECT_DIR/src/algorithms
mkdir -p $PROJECT_DIR/src/utils
mkdir -p $PROJECT_DIR/src/models
mkdir -p $PROJECT_DIR/tests/unit_tests
mkdir -p $PROJECT_DIR/tests/integration_tests
mkdir -p $PROJECT_DIR/data
mkdir -p $PROJECT_DIR/docs
mkdir -p $PROJECT_DIR/scripts
mkdir -p $PROJECT_DIR/notebooks
mkdir -p $PROJECT_DIR/config
mkdir -p $PROJECT_DIR/assets

echo "Project directories created successfully."
