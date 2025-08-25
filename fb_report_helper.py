#!/usr/bin/env python3
import re
import os
import sys
from urllib.parse import quote

# ==========================
# Facebook Report Helper
# ==========================
# Legal & safe tool for internal/educational use
# Only generates report links, does NOT auto-submit anything
# ==========================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(r"""
╔════════════════════════════════╗
║   Facebook Report Helper Tool  ║
║      By Cyber Security Team    ║
║            ZERO-WAVE-0         ║
╚════════════════════════════════╝
    """)

def extract_username(profile_url):
    """Extract Facebook username or ID from URL"""
    match = re.search(r"facebook\.com/([A-Za-z0-9\.]+)", profile_url)
    if match:
        return match.group(1)
    return None

def generate_report_links(username):
    """Generate report links for harassment, abuse, etc."""
    base_form = "https://www.facebook.com/help/contact/228813257197480"
    # Encode username to be safe for URL
    encoded_user = quote(username)
    full_link = f"{base_form}?profile={encoded_user}"
    return full_link

def main():
    clear_screen()
    banner()
    
    try:
        profile_url = input("👉 Enter Facebook Profile URL: ").strip()
        if not profile_url:
            print("❌ No URL entered. Exiting.")
            sys.exit(0)

        username = extract_username(profile_url)
        if not username:
            print("❌ Invalid Facebook profile URL!")
            sys.exit(0)
        
        report_link = generate_report_links(username)
        print("\n✅ Report this profile here (open in browser):")
        print(report_link)

        # Optional: save link to local log file
        save = input("\n💾 Save this link to log file? [y/n]: ").strip().lower()
        if save == 'y':
            with open("report_links.txt", "a") as f:
                f.write(f"{username} -> {report_link}\n")
            print("✅ Link saved to report_links.txt")

    except KeyboardInterrupt:
        print("\n❌ Interrupted by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
