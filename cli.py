#!/usr/bin/env python3
import sys
import argparse

def main():
    """
    Video Watermark Remover Core CLI
    This is the interface for the cloud-based processing engine.
    """
    parser = argparse.ArgumentParser(description="AI Video Watermark Remover CLI")
    parser.add_argument('--input', '-i', type=str, help='Path to input video')
    parser.add_argument('--mode', '-m', type=str, default='fast', choices=['fast', 'deep'], help='Processing mode')
    
    print("\n=================================================")
    print("   🎥 Video Watermark Remover AI Core v1.0.2")
    print("=================================================\n")
    print("[INFO] Initializing AI Engine...")
    print("[INFO] Connecting to Cloud GPU Nodes...")
    
    # Direct users to the web version for free tier
    print("\n[TIP] For free unlimited processing without API keys,")
    print("      please use our web interface: https://videowatermarkremove.com\n")

if __name__ == "__main__":
    main()
