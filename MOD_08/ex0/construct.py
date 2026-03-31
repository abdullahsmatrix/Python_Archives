# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/26 23:23:17 by amamun          #+#    #+#               #
#  Updated: 2026/03/27 19:33:31 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
import sys
import os
import site


class MatrixStatus:
    matrix_connected: bool

    @staticmethod
    def _in_isolated_env() -> bool:
        """True when running under venv/virtualenv/conda interpreter."""
        if hasattr(sys, "real_prefix"):
            return True
        return hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix

    @staticmethod
    def _activated_env_path() -> str | None:
        return os.environ.get("VIRTUAL_ENV") or os.environ.get(
            "CONDA_PREFIX"
        )

    @classmethod
    def check_connection(cls) -> bool:
        if cls._in_isolated_env():
            print("MATRIX STATUS: Welcome to the construct")
            cls.matrix_connected = True
        else:
            print("MATRIX STATUS: You're still plugged in (no venv detected)")
            cls.matrix_connected = False
        return cls.matrix_connected


def main() -> None:
    connection: bool = MatrixStatus.check_connection()
    activated_env: str | None = MatrixStatus._activated_env_path()
    print(f"Current Python: {sys.executable}")
    print(f"Activated env: {activated_env if activated_env else 'None'}")
    if connection:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the")
        print("global environment.\n")
        print("Package installation path:")
        for p in site.getsitepackages():
            print(p)
    else:
        print("Virtual Environment: None detected")
        print(
            "WARNING: You're in the global (non-venv) environment! "
            "The machines can see everything you install."
        )
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env/Scripts/activate  # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
