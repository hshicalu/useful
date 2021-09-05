
# Colabでドライブをマウントするおまじない

from google.colab import drive
drive.mount('/content/drive')

# GPUを使うときのおまじない

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
