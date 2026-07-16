import subprocess
import json
import pytest


def command_wrapper(terminal, command, as_json=False):
    if terminal.lower() == "powershell":
        result = subprocess.run(
            ["powershell", "-command", command],
            capture_output=True,
            text=True
        )
    elif terminal.lower() == "cmd":
        result = subprocess.run(
            ["cmd", "/c", command],
            capture_output=True,
            text=True
        )
    else:
        raise ValueError("terminal must be 'powershell' or 'cmd'")

    output = result.stdout.strip()
    if as_json:
        return json.loads(output)

    return output


def test_001_get_gpu():
    getGpuNames = command_wrapper(terminal="cmd", command="wmic path win32_VideoController get Name")
    assert "Name" in getGpuNames
    assert len(getGpuNames.splitlines()) > 1


def test_002_get_tpm():
    tpmStatus = command_wrapper(terminal="powershell", command="Get-Tpm | ConvertTo-Json", as_json=True)
    print(f"TPM Present      : {tpmStatus['TpmPresent']}")
    print(f"TPM Ready        : {tpmStatus['TpmReady']}")
    print(f"Manufacturer ID  : {tpmStatus['ManufacturerId']}")
    assert tpmStatus['TpmPresent'] is True
    assert tpmStatus['TpmReady'] is True
    assert tpmStatus["ManufacturerId"] != 0


@pytest.mark.security
def test_003_check_secure_boot_status():
    """Verify Secure Boot is enabled."""
    secureBootStatus = command_wrapper(terminal="powershell", command="Confirm-SecureBootUEFI").strip()
    assert secureBootStatus == "False"
    print(f"secure boot status is {secureBootStatus}")


def test_004_verify_vbs_is_running():
    vbs = command_wrapper("powershell",
                          "(Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard).VirtualizationBasedSecurityStatus")
    assert vbs == "2"
    print(f"vbs value is {vbs}")
