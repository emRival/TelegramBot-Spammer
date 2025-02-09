import subprocess
import re

# File yang ingin dianalisis
script_file = "tele-spam.py"

# Ambil daftar dependensi yang diimpor
dependencies = set()
with open(script_file, "r") as f:
    for line in f:
        match = re.match(r"^\s*(?:import|from) (\S+)", line)
        if match:
            package = match.group(1).split(".")[0]  # Ambil modul utama
            dependencies.add(package)

# Mapping antara nama modul Python dan paket Conda (karena ada perbedaan nama)
pip_packages = {"requests", "telegram"}  # Pastikan ini diinstal via pip
conda_mapping = {
    "cv2": "opencv",
    "np": "numpy",
    "pd": "pandas",
    "dlib": "dlib",
    "asyncio": "python",
    "requests": "requests",
    "telegram": "python-telegram-bot",
}

# Pisahkan mana yang masuk ke Conda dan mana yang perlu di-pip
conda_packages = {conda_mapping.get(pkg, pkg) for pkg in dependencies if pkg not in pip_packages}
pip_deps = {pkg for pkg in dependencies if pkg in pip_packages}

# Format environment.yml
environment_content = f"""name: attandance
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
""" + "".join(f"  - {pkg}\n" for pkg in sorted(conda_packages))

# Tambahkan dependensi pip jika ada
if pip_deps:
    environment_content += "  - pip\n  - pip:\n" + "".join(f"      - {pkg}\n" for pkg in sorted(pip_deps))

# Simpan ke environment.yml
with open("environment.yml", "w") as f:
    f.write(environment_content)

print("✅ File environment.yml berhasil dibuat berdasarkan dependensi yang digunakan di bot-tele.py!")
