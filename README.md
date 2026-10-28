# Azure VM Web Server Deployment Design

## Project status

**Status: Design and portfolio demo completed. Live Azure deployment: not performed.**

This beginner project documents how an Ubuntu Linux virtual machine on Microsoft Azure can host a static website using Nginx. The portfolio page itself can be published for free with GitHub Pages. Publishing this repository does **not** create an Azure VM.

## Objectives

- Understand the planned Azure VM web-server architecture.
- Document Azure networking components: Virtual Network, subnet, public IP and Network Security Group (NSG).
- Practice the Linux/Nginx deployment workflow.
- Publish a static portfolio page with GitHub Pages.
- Prepare a clear starting point for a future hands-on Azure deployment.

## Architecture

Open [`architecture.svg`](architecture.svg) for the diagram.

Request flow:

1. A visitor opens the website in a browser.
2. In the planned Azure deployment, traffic reaches the VM public IP.
3. An NSG permits HTTP TCP/80 to the web server.
4. Nginx on Ubuntu serves the HTML website.
5. SSH TCP/22 should be restricted to the administrator's IP address.

## Technologies

- Microsoft Azure (planned target platform)
- Ubuntu Linux (planned VM operating system)
- Nginx (planned web server)
- Azure Virtual Network, subnet, public IP and NSG (planned networking)
- HTML and CSS
- GitHub and GitHub Pages (for this portfolio demo)

## Files

- `index.html` — responsive portfolio project page
- `architecture.svg` — editable vector architecture diagram
- `README.md` — project documentation

## Publish the portfolio demo with GitHub Pages

1. Create a **public** GitHub repository named `azure-vm-webserver-project`.
2. Upload `index.html`, `architecture.svg` and `README.md` to the repository root.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/ (root)`, then save.
6. Wait for the deployment to finish. GitHub Pages will show the published URL in the Pages settings.

The page can take a few minutes to become available.

## Future Azure implementation steps

1. Create a dedicated Resource Group.
2. Deploy an Ubuntu Linux VM and configure SSH key authentication.
3. Use an NSG to allow HTTP TCP/80 and restrict SSH TCP/22 to your own IP.
4. SSH to the VM, update packages and install Nginx.
5. Copy the website file to `/var/www/html/index.html`.
6. Verify Nginx is active and test the HTTP response.
7. Add genuine screenshots and test results to this repository.
8. Delete the lab resources when finished, after checking for any resources that must be retained.

## Example commands for the future Azure VM

Run these **inside the Ubuntu VM after creating it**; they do not run on GitHub Pages:

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable --now nginx
sudo systemctl is-active nginx
curl -I http://localhost
```

Expected checks: Nginx reports `active`, and a successfully served page returns an HTTP `200 OK` response.

## Security and cost notes

- Never commit a private SSH key, passwords, tokens or other secrets.
- Restrict SSH (TCP/22) to your administrator IP; do not expose SSH to the entire internet.
- Only expose ports required for the project.
- Azure compute, disks, public IPs and other resources can incur charges. Check current pricing and your subscription terms before deployment, set a budget alert where available, and remove lab resources after use.
- GitHub Pages hosts only the static portfolio files; it does not run the planned Azure VM.

## Resume wording

Use wording that matches the work actually completed.

**After publishing this design demo only:**
> Designed and documented an Azure VM web-server deployment architecture, including Ubuntu, Nginx, networking and NSG security rules; published a static project portfolio using GitHub Pages.

**Only after performing and testing the real Azure deployment:**
> Deployed a website on an Azure Ubuntu VM using Nginx; configured NSG inbound rules and validated HTTP access.

## Learning outcome

This project provides a documented foundation for learning Azure compute, Linux administration, networking and web-server operations. The next step is to perform the actual deployment in an Azure environment when an eligible subscription is available.


## Automated checks with GitHub Actions

This repository includes a small Python test suite and a GitHub Actions workflow. On every push or pull request, the workflow checks that required files exist, that the HTML contains expected project sections, and that the README clearly states the Azure deployment has not yet been performed.

### Run tests locally on Windows

Install Python 3 if it is not already installed, then open PowerShell in the repository folder and run:

```powershell
py -m unittest discover -s tests -v
```

All tests should pass. If `py` is not recognized, install Python from https://www.python.org/downloads/windows/ and select **Add Python to PATH** during installation.

### Enable GitHub Actions

Upload the `.github/workflows/portfolio-checks.yml` file and `tests/test_portfolio.py` to the repository. Open the **Actions** tab and check the latest workflow run. A green check means the automated checks passed.

This workflow tests the static project files. It does not provision, deploy or test a live Azure VM.
