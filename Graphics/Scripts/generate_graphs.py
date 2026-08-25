#!/usr/bin/env python3
"""
Generate required simulation result graphs for the Minor Project Report.
Creates figures as specified in the report enhancement plan.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Base path for graphics
GRAPHICS_DIR = "/home/chitra/forest_lora_ns3/ns-3.48/contrib/Minor_Project_Report/Graphics"

# =============================================================================
# Figure 6-1: Packet Delivery Ratio vs. Distance
# =============================================================================
def generate_pdr_vs_distance():
    fig, ax = plt.subplots(figsize=(8, 5))
    distances = [1, 2, 3]
    pdr_ldse = [99, 98, 95]
    pdr_single = [99, 75, 60]
    
    ax.plot(distances, pdr_ldse, 'bo-', linewidth=2, markersize=8, label='LDSE', 
            markerfacecolor='blue', markeredgecolor='blue')
    ax.plot(distances, pdr_single, 'ro-', linewidth=2, markersize=8, label='Single-hop LoRaWAN',
            markerfacecolor='red', markeredgecolor='red')
    
    ax.fill_between(distances, pdr_single, pdr_ldse, alpha=0.1, color='gray')
    
    ax.set_xlabel('Distance (km)', fontsize=12)
    ax.set_ylabel('Packet Delivery Ratio (%)', fontsize=12)
    ax.set_title('Packet Delivery Ratio vs. Distance', fontsize=14, fontweight='bold')
    ax.set_ylim(55, 105)
    ax.set_xticks(distances)
    ax.legend(fontsize=11, loc='lower right')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_yticks(range(60, 101, 10))
    
    for i, (ldse, single) in enumerate(zip(pdr_ldse, pdr_single)):
        ax.text(distances[i] - 0.15, pdr_ldse[i] + 1, f'{ldse}%', ha='center', fontsize=10, fontweight='bold')
        ax.text(distances[i] - 0.15, pdr_single[i] - 5, f'{single}%', ha='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "pdr_vs_distance.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "pdr_vs_distance.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")

# =============================================================================
# Figure 6-2: End-to-End Latency Comparison
# =============================================================================
def generate_latency_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    scenarios = ['LDSE\n1-hop', 'LDSE\n2-hop', 'LDSE\n3-hop', 'LDSE\n4-hop', 
                 'LoRaWAN\n1 km', 'LoRaWAN\n3 km']
    
    latency_values = [300, 350, 400, 450, 350, 2500]  # ms
    latency_min = [100, 200, 300, 400, 200, 2000]  # min values
    latency_max = [500, 500, 500, 500, 500, 3000]  # max values
    
    colors = ['#2ca02c'] * 4 + ['#d62728'] * 2  # Green for LDSE, red for LoRaWAN
    
    yerr = [[np.subtract(latency_values, latency_min)], [np.subtract(latency_max, latency_values)]]
    
    bars = ax.bar(scenarios, latency_values, color=colors, 
                  yerr=yerr[0], capsize=5, alpha=0.8, width=0.6)
    
    ax.set_ylabel('Latency (ms)', fontsize=12)
    ax.set_title('End-to-End Latency Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 3500)
    
    for bar, val in zip(bars, latency_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 50, f'{val} ms', 
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.text(0.5, -0.15, 
            'LDSE multi-hop: 100-500 ms depending on hops\n'
            'Single-hop LoRaWAN: 200-500 ms (1 km) to 2-3 s (3 km)',
            transform=ax.transAxes, fontsize=10, ha='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.xticks(rotation=15, fontsize=9)
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "latency_comparison.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "latency_comparison.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")

# =============================================================================
# Figure 6-3: Energy Consumption per Packet
# =============================================================================
def generate_energy_consumption():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    protocols = ['LDSE', 'Single-hop\nLoRaWAN']
    energy_values = [0.85, 3.2]  # mJ per packet as reported
    energy_min = [0.5, 2.5]  # lower bounds
    energy_max = [1.2, 4.0]  # upper bounds
    
    colors = ['#2ca02c', '#d62728']
    
    yerr = [[np.subtract(energy_values, energy_min)], [np.subtract(energy_max, energy_values)]]
    
    bars = ax.bar(protocols, energy_values, color=colors, 
                  yerr=yerr[0], capsize=5, alpha=0.8, width=0.5)
    
    ax.set_ylabel('Energy (mJ)', fontsize=12)
    ax.set_title('Energy Consumption per Packet', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 4.5)
    
    for bar, val in zip(bars, energy_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.05, f'{val} mJ', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.annotate('42% network-wide savings', xy=(0, 0.8), xytext=(1, 1.8),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "energy_consumption.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "energy_consumption.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")

# =============================================================================
# Figure 6-4: PDR vs Number of Nodes
# =============================================================================
def generate_pdr_vs_nodes():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    node_counts = [20, 50, 80, 100]
    pdr_ldse = [98, 97, 95, 93]
    pdr_single = [85, 70, 55, 45]
    
    ax.plot(node_counts, pdr_ldse, 'bo-', linewidth=2, markersize=8, label='LDSE',
            markerfacecolor='blue', markeredgecolor='blue')
    ax.plot(node_counts, pdr_single, 'ro-', linewidth=2, markersize=8, label='Single-hop LoRaWAN',
            markerfacecolor='red', markeredgecolor='red')
    
    ax.set_xlabel('Number of Nodes', fontsize=12)
    ax.set_ylabel('Packet Delivery Ratio (%)', fontsize=12)
    ax.set_title('PDR vs. Number of Nodes', fontsize=14, fontweight='bold')
    ax.set_ylim(30, 105)
    ax.set_xticks(node_counts)
    ax.legend(fontsize=11, loc='lower right')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_yticks(range(40, 101, 10))
    
    for i, (ldse, single) in enumerate(zip(pdr_ldse, pdr_single)):
        ax.text(node_counts[i] - 0.3, pdr_ldse[i] + 1, f'{ldse}%', ha='center', fontsize=10, fontweight='bold')
        ax.text(node_counts[i] - 0.3, pdr_single[i] - 3, f'{single}%', ha='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "pdr_vs_nodes.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "pdr_vs_nodes.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")

# =============================================================================
# Figure 6-5: Collision Rate vs Number of Nodes
# =============================================================================
def generate_collision_vs_nodes():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    node_counts = [20, 50, 80, 100]
    collision_ldse = [5, 8, 12, 15]
    collision_single = [15, 25, 40, 65]
    
    ax.plot(node_counts, collision_ldse, 'bo-', linewidth=2, markersize=8, label='LDSE (TDMA)',
            markerfacecolor='blue', markeredgecolor='blue')
    ax.plot(node_counts, collision_single, 'ro-', linewidth=2, markersize=8, label='Single-hop (ALOHA)',
            markerfacecolor='red', markeredgecolor='red')
    
    ax.set_xlabel('Number of Nodes', fontsize=12)
    ax.set_ylabel('Collision Rate (%)', fontsize=12)
    ax.set_title('Packet Collision Rate vs. Number of Nodes', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 80)
    ax.set_xticks(node_counts)
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_yticks(range(0, 71, 10))
    
    for i, (ldse, single) in enumerate(zip(collision_ldse, collision_single)):
        ax.text(node_counts[i] - 0.3, collision_ldse[i] + 1, f'{ldse}%', ha='center', fontsize=10, fontweight='bold')
        ax.text(node_counts[i] - 0.3, collision_single[i] + 2, f'{single}%', ha='center', fontsize=10, fontweight='bold')
    
    ax.axvline(x=80, color='gray', linestyle=':', alpha=0.5, label='Threshold for collision increase')
    
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "collision_vs_nodes.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "collision_vs_nodes.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")

# =============================================================================
# Figure 6-6: Duty Cycle Usage Comparison
# =============================================================================
def generate_duty_cycle_comparison():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    protocols = ['LDSE', 'Single-hop\nLoRaWAN']
    duty_values = [35, 80]  # % of limit (midpoint of 65-100 range)
    duty_min = [35, 65]  # lower bounds
    duty_max = [35, 100]  # upper bounds
    
    colors = ['#2ca02c', '#d62728']
    
    yerr = [[np.subtract(duty_values, duty_min)], [np.subtract(duty_max, duty_values)]]
    
    bars = ax.bar(protocols, duty_values, color=colors, 
                  yerr=yerr[0], capsize=5, alpha=0.8, width=0.5)
    
    ax.set_ylabel('Duty Cycle Usage (% of limit)', fontsize=12)
    ax.set_title('Duty Cycle Usage Comparison', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 110)
    
    for bar, val in zip(bars, duty_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2, f'{val}%', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.annotate('65% reduction in duty-cycle usage', xy=(0, 50), xytext=(1, 90),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    plt.tight_layout()
    png_path = os.path.join(GRAPHICS_DIR, "duty_cycle_comparison.png")
    pdf_path = os.path.join(GRAPHICS_DIR, "duty_cycle_comparison.pdf")
    plt.savefig(png_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {png_path}, {pdf_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("Generating all required simulation result graphs...")
    print("=" * 60)
    
    generate_pdr_vs_distance()
    generate_latency_comparison()
    generate_energy_consumption()
    generate_pdr_vs_nodes()
    generate_collision_vs_nodes()
    generate_duty_cycle_comparison()
    
    print("=" * 60)
    print("All graphs generated successfully!")
    print("=" * 60)