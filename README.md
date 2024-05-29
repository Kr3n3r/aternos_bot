<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Kr3n3r/aternos_bot/">
    <img src="zzz_readme_src/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">aternos_bot</h3>

  <p align="center">
    (Telegram) bot to manage Aternos servers
    <br />
    <a href="https://github.com/Kr3n3r/aternos_bot/tree/main/docs"><strong>Documentation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Kr3n3r/aternos_bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Kr3n3r/aternos_bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()

(Telegram) bot to manage Aternos servers

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [aiogram]()
* [environs]()
* [python_aternos]()
* [Babel]()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow the instructions to install and execute bot in poolling mode.

### Prerequisites

* Python >= 3.10.0
* An Aternos account that have the following access to a server(you can grant them from "Access" bar)
```
Start
Stop/Restart
TODO
``` 
* (Optional) For Telegram integration:
  * An BOT API KEY. Talk to BotFather to obtain it
  ```sh
  https://t.me/BotFather
  ```
  * IDs of admin users that want to operate with the bot. You can obtain your personal ID talking with
  ```sh
  https://t.me/getmyid_bot
  ```

### Installation

1. Read README and visit github to search for issues.
2. Clone repo
   ```sh
   git clone https://github.com/Kr3n3r/aternos_bot.git
   ```
3. Rename .env.dist to .env and fill variables with data
   ```sh
   .env.dist -> .env
   ```
4. Execute start.bat
   ```sh
   start.bat
   ```

You can also use the Docker image uploaded in public repository(https://hub.docker.com/repository/docker/kr3n3r/aternos_bot/general). Just run the following command
   ```sh
   docker run -it kr3n3r/aternos_bot:<version>
   ```
Variables for build
* BASE_IMAGE: Which image to use. See docker-compose.yml for more info.

Variables for use
* ADMIN: Telegram ID of users that can interact with bot
* TELEGRAM_TOKEN: Telegram Token
* LOCALE: possible values
  * en
  * ru
* ATERNOS_LOGIN: user for Aternos
* ATERNOS_PASS: password for Aternos
* ATERNOS_PASS_HASH: hash password for Aternos
* TZ: timezone for time displayed. For example, Europe/Madrid

Images in registry are only compatible with arm64v8 architectures(for RaspberryPI 5 purpose).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Deploy the app and talk to the bot to manage Aternos servers

_For more examples, please refer to the [Documentation](https://github.com/Kr3n3r/aternos_bot/blob/main/docs/)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Launch first version
- [x] Integrate with Docker
- [ ] Bug resolution: concurrent server actions
- [ ] Integration with Discord / Whatsapp

See the [open issues](https://github.com/Kr3n3r/aternos_bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

See License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@Kren3r](https://twitter.com/Kren3r) - marmolromeroalejandro@gmail.com

Project Link: [https://github.com/Kr3n3r/aternos_bot/](https://github.com/Kr3n3r/aternos_bot/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Kr3n3r/atlas_bot.svg?style=for-the-badge
[contributors-url]: https://github.com/Kr3n3r/atlas_bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kr3n3r/atlas_bot.svg?style=for-the-badge
[forks-url]: https://github.com/Kr3n3r/atlas_bot/network/members
[stars-shield]: https://img.shields.io/github/stars/Kr3n3r/atlas_bot.svg?style=for-the-badge
[stars-url]: https://github.com/Kr3n3r/atlas_bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kr3n3r/atlas_bot.svg?style=for-the-badge
[issues-url]: https://github.com/Kr3n3r/atlas_bot/issues
[license-shield]: https://img.shields.io/github/license/Kr3n3r/atlas_bot.svg?style=for-the-badge
[license-url]: https://github.com/Kr3n3r/atlas_bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alejandro-marmol-romero-885376229
[product-screenshot]: TODO
