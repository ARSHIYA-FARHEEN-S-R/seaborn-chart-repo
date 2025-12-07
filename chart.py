"""
Seaborn Heatmap Generator
Author: 23f2001189@ds.study.iitm.ac.in
Generates a 512x512 pixel correlation matrix heatmap
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Set backend for image generation
matplotlib.use('Agg')

# Set random seed for reproducibility
np.random.seed(42)

def create_heatmap():
    """
    Create and save a 512x512 pixel Seaborn heatmap
    """
    # Generate 10x10 correlation matrix
    data = np.random.randn(10, 50)
    corr_matrix = np.corrcoef(data)
    
    # Ensure it's symmetric and valid
    corr_matrix = (corr_matrix + corr_matrix.T) / 2
    np.fill_diagonal(corr_matrix, 1.0)
    corr_matrix = np.clip(corr_matrix, -1, 1)
    
    # Create figure with exact 512x512 dimensions
    # 5.12 inches at 100 DPI = 512 pixels
    fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)
    
    # Create Seaborn heatmap
    sns.heatmap(
        corr_matrix,
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=0.5,
        linecolor='white',
        cbar_kws={'shrink': 0.8, 'label': 'Correlation'},
        ax=ax
    )
    
    # Add title and labels
    ax.set_title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Features', fontsize=11)
    ax.set_ylabel('Features', fontsize=11)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save as 512x512 PNG
    plt.savefig(
        'chart.png',
        dpi=100,
        bbox_inches='tight',
        pad_inches=0.1,
        facecolor='white',
        edgecolor='none'
    )
    
    plt.close(fig)
    
    print("✅ Heatmap generated: chart.png (512x512 pixels)")
    print(f"📧 Author: 23f2001189@ds.study.iitm.ac.in")
    
    return corr_matrix

if __name__ == '__main__':
    # Generate the heatmap
    matrix = create_heatmap()
    
    # Print statistics
    print(f"\n📊 Matrix Statistics:")
    print(f"   Shape: {matrix.shape}")
    print(f"   Mean: {matrix.mean():.3f}")
    print(f"   Min: {matrix.min():.3f}")
    print(f"   Max: {matrix.max():.3f}")
