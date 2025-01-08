<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Follower Remover Script</title>
</head>
<body>
    <h1>Instagram Follower Remover Script</h1>
    <p>
        This script automates the process of removing followers from your Instagram account. It allows you to clear out unwanted followers or reduce spam manually by removing all followers directly from your account.
    </p>
    <blockquote>
        <strong>Note:</strong> The script does not identify spammers automatically; it simply removes all followers from your account when executed.
    </blockquote>

<h2>Features</h2>
    <ul>
        <li>Automates logging into your Instagram account.</li>
        <li>Removes all followers from your account in bulk.</li>
        <li>Helps in decluttering your account and clearing spam followers.</li>
    </ul>

<h2>Requirements</h2>
    <ol>
        <li><strong>Python 3.7+</strong></li>
        <li>Required libraries:
            <ul>
                <li><code>selenium</code></li>
                <li><code>time</code></li>
                <li><code>os</code></li>
            </ul>
        </li>
    </ol>

 <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/adityapatilDU/instagram-follower-remover.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd instagram-follower-remover</code></pre>
        </li>
        <li>Install the required libraries:
            <pre><code>pip install selenium</code></pre>
        </li>
    </ol>

<h2>Setup</h2>
    <ol>
        <li>Download the ChromeDriver compatible with your browser version from <a href="https://chromedriver.chromium.org" target="_blank">chromedriver.chromium.org</a>.</li>
        <li>Place the downloaded ChromeDriver in your project directory.</li>
        <li>Update the script to include the path to the ChromeDriver.</li>
    </ol>

<h2>Usage</h2>
    <ol>
        <li>Run the script:
            <pre><code>python follower_remover.py</code></pre>
        </li>
        <li>Log in to your Instagram account through the automated browser window.</li>
        <li>The script will begin removing all followers from your account.</li>
    </ol>

 <h2>Disclaimer</h2>
    <p>
        <strong>Important:</strong>
        <ul>
            <li>This script is for <strong>educational purposes only</strong>.</li>
            <li>Use responsibly and ensure compliance with Instagram's terms of service.</li>
            <li>Removing all followers will clear your follower list entirely.</li>
        </ul>
    </p>
</body>
</html>
