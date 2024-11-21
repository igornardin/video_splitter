# Video splitter

Video splitter is a Python library for splitting one video into different videos.

## Installation

Use the [NixOS](https://nixos.org/) to install.

```bash
cd video_splitter/
nix-shell
```

## Usage
Put all your mp4 files inside the folder input. Then, create an **input.csv** inside this folder, as follows: 

```csv
prefix,input_mp4,surname,begin,end
conf_2024,video1203312642.mp4,test,00:03:50,00:08:40
conf_2024,video1203312642.mp4,teste_2,00:09:28,00:48:30
```
where:

- **prefix** is the prefix used for the output files;
- **input_mp4** is the mp4 inside the input folder
- **surname** is the suffix for the output files;
- **begin** is the time (format hh:mm:ss) that the presenter starts;
- **end** is the time (format hh:mm:ss) that the presenter finishes;

Then, it needs to execute:
```
python converter.py
```

It will create a mp4 file for each line of **input.csv**, extracting from the original **input_mp4** file.

## License

[MIT](https://choosealicense.com/licenses/mit/)
