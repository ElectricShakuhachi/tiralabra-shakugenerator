from interfaces.interfaces import ShakuGeneratorInterfaceManager

if __name__ == "__main__":
    """Start Shakugenerator when running it as standalone from cli.
    We do not load dotenv here because this part is bypassed when
    using Shakugenerator as plugin.
    """
    interface = ShakuGeneratorInterfaceManager("cli")
    interface.start()
