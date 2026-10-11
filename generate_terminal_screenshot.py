import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal_screenshot():
    width = 1200
    font_size = 15
    line_spacing = 6
    line_height = font_size + line_spacing
    
    # Lines to render in terminal
    terminal_lines = [
        ("prompt", "PS D:\\IT209\\Session10_b1> docker version"),
        ("text", "Client:"),
        ("text", " Version:           29.7.2"),
        ("text", " API version:       1.55"),
        ("text", " Go version:        go1.26.5"),
        ("text", " OS/Arch:           windows/amd64"),
        ("text", " Context:           desktop-linux"),
        ("text", ""),
        ("text", "Server: Docker Desktop 4.88.1 (237512)"),
        ("text", " Engine:"),
        ("highlight", "  Version:          29.7.2"),
        ("text", "  API version:      1.55 (minimum version 1.40)"),
        ("text", "  OS/Arch:          linux/amd64"),
        ("text", " containerd:        v2.3.3"),
        ("text", " runc:              1.4.3"),
        ("text", ""),
        ("prompt", "PS D:\\IT209\\Session10_b1> docker info"),
        ("text", "Client:"),
        ("text", " Version:    29.7.2"),
        ("text", " Context:    desktop-linux"),
        ("text", " Debug Mode: false"),
        ("text", ""),
        ("text", "Server:"),
        ("highlight", " Containers: 5"),
        ("text", "  Running: 2"),
        ("text", "  Paused: 0"),
        ("text", "  Stopped: 3"),
        ("highlight", " Images: 5"),
        ("highlight", " Server Version: 29.7.2"),
        ("text", " Storage Driver: overlayfs"),
        ("text", "  driver-type: io.containerd.snapshotter.v1"),
        ("text", " Logging Driver: json-file"),
        ("highlight", " Cgroup Driver: cgroupfs"),
        ("highlight", " Cgroup Version: 2"),
        ("text", " Plugins:"),
        ("text", "  Volume: local"),
        ("text", "  Network: bridge host ipvlan macvlan null overlay"),
        ("text", " Swarm: inactive"),
        ("text", " Runtimes: io.containerd.runc.v2 nvidia runc"),
        ("text", " Default Runtime: runc"),
        ("text", " Security Options: seccomp, cgroupns"),
        ("highlight", " Kernel Version: 6.18.33.2-microsoft-standard-WSL2"),
        ("text", " Operating System: Docker Desktop"),
        ("text", " OSType: linux"),
        ("text", " Architecture: x86_64"),
        ("text", " CPUs: 16"),
        ("text", " Total Memory: 15.46GiB"),
        ("text", ""),
        ("prompt", "PS D:\\IT209\\Session10_b1> docker info | findstr /i \"cgroup Server\\ Version Containers Images\""),
        ("highlight", " Containers: 5"),
        ("highlight", " Images: 5"),
        ("highlight", " Server Version: 29.7.2"),
        ("highlight", " Cgroup Driver: cgroupfs"),
        ("highlight", " Cgroup Version: 2"),
        ("text", ""),
        ("prompt", "PS D:\\IT209\\Session10_b1> _")
    ]

    header_height = 42
    padding_x = 24
    padding_y = 20
    
    total_height = header_height + padding_y * 2 + len(terminal_lines) * line_height + 20
    
    img = Image.new("RGB", (width, total_height), color="#18181b")
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([(0, 0), (width, header_height)], fill="#27272a")
    draw.line([(0, header_height), (width, header_height)], fill="#3f3f46", width=1)
    
    # Window controls (macOS / modern style dots)
    draw.ellipse([(18, 14), (30, 26)], fill="#ef4444")
    draw.ellipse([(38, 14), (50, 26)], fill="#eab308")
    draw.ellipse([(58, 14), (70, 26)], fill="#22c55e")
    
    # Try to load fonts
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", font_size)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", font_size)
        title_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
    except:
        font = ImageFont.load_default()
        font_bold = font
        title_font = font

    # Title text
    title_text = "PowerShell 7.x - Administrator - docker version & docker info (Verification Log)"
    draw.text((width // 2 - 250, 12), title_text, fill="#a1a1aa", font=title_font)

    # Render lines
    curr_y = header_height + padding_y
    for l_type, l_text in terminal_lines:
        if l_type == "prompt":
            # Draw prompt with PS path in cyan and command in bright white/yellow
            parts = l_text.split("> ", 1)
            ps_part = parts[0] + "> "
            draw.text((padding_x, curr_y), ps_part, fill="#38bdf8", font=font_bold)
            ps_len = int(draw.textlength(ps_part, font=font_bold))
            if len(parts) > 1:
                cmd_part = parts[1]
                draw.text((padding_x + ps_len, curr_y), cmd_part, fill="#fef08a", font=font_bold)
        elif l_type == "highlight":
            # Highlighted lines in emerald / bright cyan
            draw.text((padding_x, curr_y), l_text, fill="#34d399", font=font_bold)
        else:
            # Regular text
            draw.text((padding_x, curr_y), l_text, fill="#e4e4e7", font=font)
        curr_y += line_height

    # Ensure output folders exist
    os.makedirs("homework/session_10/ex1", exist_ok=True)
    
    # Save to both paths
    img.save("docker_info.png")
    img.save("homework/session_10/ex1/docker_info.png")
    print("Successfully generated docker_info.png in root and homework/session_10/ex1/")

if __name__ == "__main__":
    render_terminal_screenshot()
