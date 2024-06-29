---

# Text to Video Generation using Stable Diffusion and MoviePy

This Python script generates a video from text prompts using Stable Diffusion for image generation and MoviePy for video creation. It's a great way to explore AI-powered video creation directly from textual descriptions.

## Installation

### Prerequisites

Before you begin, make sure you have Python 3.x installed on your system.

### Clone the Repository

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

### Install Dependencies

1. Install required Python libraries using pip:

   ```bash
   pip install torch Pillow moviepy diffusers
   ```

   - `torch`: PyTorch library for machine learning.
   - `Pillow`: Python Imaging Library for image processing.
   - `moviepy`: Library for video editing and creation.
   - `diffusers`: Library for utilizing Stable Diffusion models.

## Usage

1. Open `text_to_video.py` in a text editor or Python IDE.

2. Modify the `prompts` list to add or change the text prompts for generating different videos.

3. Save your changes.

4. Run the script using Python:

   ```bash
   python text_to_video.py
   ```

   This script will use your GPU if available (recommended for faster processing) or fall back to CPU.

5. Once the script finishes running, check the project directory for the generated video file named `output_video.mp4`.

## Example Prompts

The script includes predefined text prompts like:

- "A serene landscape with mountains"
- "A bustling city at night"
- "A calm beach with a sunset"

Modify these prompts directly in the script to generate videos matching your imagination.

## Notes

- Adjust the frame rate (`fps`) in the `ImageSequenceClip` constructor inside `text_to_video.py` to control the video's speed and smoothness.

---
