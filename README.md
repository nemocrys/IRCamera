# IRCamera

Record infrared images with an Optris PI640 Camera on Linux.

The project is developed and maintained by the [**Model experiments group**](https://www.ikz-berlin.de/en/research/materials-science/section-fundamental-description#c486) at the Leibniz Institute for Crystal Growth (IKZ).

### Referencing
If you use this code in your research, please cite our article:

> A. Enders-Seidlitz, J. Pal, and K. Dadzis, Model experiments for Czochralski crystal growth processes using inductive and resistive heating *IOP Conference Series: Materials Science and Engineering, Electromagnetic Processing of Materials (EPM 2021)*, 2022, In press.

## Usage

To record images use the script *run_ircamera.py* and the parameter file *settings.yml*.

There is an issue with the configuration of emissivities, currently only a value of 1 can be set.

The IR Camera is configured in *20112117.xml* (only valid for the specific device used in the NEMOCRYS project, [adjustment required for other cameras](http://documentation.evocortex.com/libirimager2/html/Installation.html)) and accessed using the Camera class defined in *ircamera.py*. FiloCara's interface [pyoptris](https://github.com/FiloCara/pyOptris/blob/dev/setup.py) is used for accessing the camera, it's located in the *source* direcotry.

## License

This code is available under a GPL v3 License. Parts are copied from [FiloCara/pyOptris](https://github.com/FiloCara/pyOptris/blob/dev/setup.py) and available under MIT License.

## Acknowledgements

Main parts of this code have been written by [Max Schröder](https://github.com/mfschroeder).

[This project](https://www.researchgate.net/project/NEMOCRYS-Next-Generation-Multiphysical-Models-for-Crystal-Growth-Processes) has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No 851768).

<img src="https://raw.githubusercontent.com/nemocrys/pyelmer/master/EU-ERC.png">

## Contribution

Any help to improve this code is very welcome!
