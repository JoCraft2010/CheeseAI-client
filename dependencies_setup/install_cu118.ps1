$packages = pip freeze

$packagesToExclude = @("pip", "setuptools", "wheel")
$packagesToUninstall = $packages | Select-String -Pattern ($packagesToExclude -join "|") -NotMatch

$packagesToUninstall | ForEach-Object {
    Write-Host "Uninstalling $($_.Line)..."
    pip uninstall -y $($_.Line)
}


pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel
pip install --upgrade pyinstaller
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install --upgrade transformers[torch]
pip install --upgrade diffusers[torch]
pip install --upgrade elevate
pip install --upgrade flask
pip install --upgrade pysimplegui
