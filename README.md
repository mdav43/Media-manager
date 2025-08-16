# Media-manager

## Running the Media Library Generator

To generate the HTML file, run the following command in your terminal:

```bash
python media_library.py
```

This will read the `config.json` file and create an `index.html` file inside the `output` directory. You can then open the `output/index.html` file in your web browser to see the media library.

### Dependencies

The script uses only standard Python libraries, so no external dependencies are required.

### Project Structure

- `media_library.py`: The main Python script that generates the HTML.
- `config.json`: The configuration file containing the media data.
- `output/`: The directory where the generated `index.html` file is saved.
- `README.md`: This file.