# Nautilus actions

Actions for Nautilus I made, based on the excellent [actions-for-nautilus](https://github.com/bassmanitram/actions-for-nautilus).

## Install

- install [actions-for-nautilus](https://github.com/bassmanitram/actions-for-nautilus)
- clone this repo
- make a link from actions-for-nautilus config file location to this project `config.json` file:

    ```bash
    mkdir -p ~/.local/share/actions-for-nautilus
    ln -s $PWD/config.json ~/.local/share/actions-for-nautilus/
    ```

    => replace $PWD by the folder you cloned this repo onto, if you're not inside this folder when you type this command
- restart Nautils
    `nautilus -q; nautilus`
