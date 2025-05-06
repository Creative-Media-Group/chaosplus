from cairosvg import svg2png

svg2png(
    url="icon.svg",
    write_to="src/assets/icon.png",
    output_width="1024",
    parent_height="1024",
)
svg2png(
    url="icon.svg",
    write_to="src/assets/splash_android.png",
    output_width="1152",
    parent_height="1152",
)
