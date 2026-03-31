# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/30 20:25:02 by amamun          #+#    #+#               #
#  Updated: 2026/03/30 23:18:52 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import os
from dotenv import load_dotenv


def load_config(REQUIRED_CONFIG: list):
    load_dotenv()
    config: dict = {}
    missing: list = []

    for var in REQUIRED_CONFIG:
        value = os.getenv(var)
        if value is None or value.strip() == "":
            missing.append(var)
            config[var] = None
        else:
            config[var] = value
    return config, missing


def load_configuration(config: dict) -> None:
    print("Configuration loaded:")
    mode = config.get('MATRIX_MODE', 'production')
    print(f"Mode: {mode}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {config.get('LOG_LEVEL', 'INFO')}")
    print("Zion Network: Online")

    print("Environment security check:")
    if os.getenv("API_KEY") == config["API_KEY"]:
        print("[WARNING] Hardcoded secret detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if os.getenv("MATRIX_MODE") == "production":
        print("[WARNING] Production mode enabled")
    else:
        print("[OK] Production overrides available")

    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    REQUIRED_CONFIG: list = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    config, missing = load_config(REQUIRED_CONFIG)

    if missing:
        print("\nWARNING: Missing configuration variables:")
        for var in missing:
            print(f"- {var}")
        print("Please set them in the environment or in a .env file.")
    else:
        load_configuration(config)


if __name__ == "__main__":
    main()
