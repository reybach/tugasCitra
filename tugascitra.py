
    image = iio.imread(image_path, mode='L')
    
    
    roberts_edges = roberts_edge_detection(image)
    sobel_edges = sobel_edge_detection(image)
    
   
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


image_path = "image.jpg"  
main(image_path)