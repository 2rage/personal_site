import subprocess
import re

def hugo_server():
    result = subprocess.run(['ip', 'addr', 'show', 'eth0'], stdout=subprocess.PIPE, text=True)
    
    ip_match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', result.stdout)
    if ip_match:
        wsl2_ipaddress = ip_match.group(1)
        subprocess.run([
            'hugo', 'server',
            '--bind', wsl2_ipaddress,
            '--baseURL', f'http://{wsl2_ipaddress}',
            '-D', '-F', '--gc', '-w'
        ])
    return

hugo_server()