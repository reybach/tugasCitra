import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Program Deteksi Tepi dengan Operator Roberts dan Sobel
# Dibuat oleh: Muhammad Reyhan Bachtiar

def roberts_edge_detection(image):
    """
    Fungsi untuk mendeteksi tepi menggunakan operator Roberts.
    Roberts menggunakan dua kernel 2x2 untuk mendeteksi tepi secara diagonal.
    """
    roberts_x = np.array([[1, 0], [0, -1]])
    roberts_y = np.array([[0, 1], [-1, 0]])
    
    edge_x = convolve(image, roberts_x)
    edge_y = convolve(image, roberts_y)
    
    edge = np.sqrt(edge_x**2 + edge_y**2)
    return edge

def sobel_edge_detection(image):
    """
    Fungsi untuk mendeteksi tepi menggunakan operator Sobel.
    Sobel menggunakan dua kernel 3x3 yang lebih besar untuk mendeteksi tepi secara vertikal dan horizontal.
    """
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    
    edge_x = convolve(image, sobel_x)
    edge_y = convolve(image, sobel_y)
    
    edge = np.sqrt(edge_x**2 + edge_y**2)
    return edge

def main(image_path):
    """
    Fungsi utama untuk membaca gambar, menerapkan deteksi tepi Roberts dan Sobel,
    serta menampilkan hasilnya menggunakan matplotlib.
    """
    # Membaca gambar dalam mode grayscale
    image = iio.imread(image_path, mode='L')
    
    # Menerapkan deteksi tepi
    roberts_edges = roberts_edge_detection(image)
    sobel_edges = sobel_edge_detection(image)
    
    # Menampilkan hasil deteksi tepi
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")
    
    plt.subplot(1, 3, 2)
    plt.imshow(roberts_edges, cmap='gray')
    plt.title("Roberts Edge Detection")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.imshow(sobel_edges, cmap='gray')
    plt.title("Sobel Edge Detection")
    plt.axis("off")
    
    plt.show()

# Contoh penggunaan
image_path = "image.jpg"  # Ganti dengan path gambar
main(image_path)