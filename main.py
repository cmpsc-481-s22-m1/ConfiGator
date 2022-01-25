name: Gradeon: [push, pull_request]

jobs:
  grade:
    runs-on: ubuntu-latest
    name: Grade
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: Run GatorGradle
        uses: GatorEducator/gatorgradle-action@v1