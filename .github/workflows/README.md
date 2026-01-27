# GitHub Actions Deployment Setup

This workflow automatically deploys the SolarityAI landing page to AWS S3 and invalidates CloudFront cache when changes are pushed to the develop branch.

## Prerequisites

- Terraform infrastructure must be deployed first
- GitHub repository must have the required secrets configured

## Required GitHub Secrets

Add these secrets in your GitHub repository settings (Settings → Secrets and variables → Actions):

### 1. AWS_ROLE_ARN

The IAM role ARN for GitHub Actions OIDC authentication.

**How to get it:**

```bash
cd terraform/solarityai-static-website
terraform output github_actions_role_arn
```

Example: `arn:aws:iam::123456789012:role/solarityai-website-github-actions-role`

### 2. S3_BUCKET_NAME

The S3 bucket name where the website files will be uploaded.

**How to get it:**

```bash
cd terraform/solarityai-static-website
terraform output s3_bucket_id
```

Example: `solarityai-website`

### 3. CLOUDFRONT_DISTRIBUTION_ID

The CloudFront distribution ID for cache invalidation.

**How to get it:**

```bash
cd terraform/solarityai-static-website
terraform output cloudfront_distribution_id
```

Example: `E1234567890ABC`

## Setup Steps

1. **Deploy Terraform infrastructure:**

   ```bash
   cd terraform/solarityai-static-website
   terraform init
   terraform plan
   terraform apply
   ```

2. **Get the outputs:**

   ```bash
   terraform output github_actions_role_arn
   terraform output s3_bucket_id
   terraform output cloudfront_distribution_id
   ```

3. **Add GitHub secrets:**
   - Go to your repository: https://github.com/Solarity-AI/solarityai-landing-page
   - Navigate to Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Add each of the three secrets above

4. **Test the workflow:**
   - Push a change to the `develop` branch
   - Check the Actions tab to see the deployment progress

## How It Works

- **Trigger:** Workflow runs on push to `develop` branch or manual trigger
- **Authentication:** Uses OIDC (no access keys needed) to assume IAM role
- **Deployment:**
  - Uploads files to S3 bucket
  - Sets appropriate cache headers (long cache for static assets, short cache for HTML)
  - Excludes unnecessary files (git, node_modules, etc.)
- **Cache Invalidation:** Creates CloudFront invalidation for all paths (`/*`)
- **Summary:** Creates a deployment summary in the GitHub Actions UI

## Cache Strategy

- **Static assets** (CSS, JS, images, fonts): `max-age=31536000, immutable` (1 year)
- **HTML files and metadata**: `max-age=0, no-store, no-cache, must-revalidate` (always fresh)

## Manual Deployment

You can manually trigger the workflow:

1. Go to the **Actions** tab in GitHub
2. Select **Deploy Static Website to AWS**
3. Click **Run workflow**
4. Select the branch (usually `develop`)
5. Click **Run workflow**

## Troubleshooting

### Error: "AWS_ROLE_ARN secret is not set"

- Make sure you've added the secret in GitHub repository settings
- Verify the secret name is exactly `AWS_ROLE_ARN` (case-sensitive)

### Error: "Access Denied" when uploading to S3

- Check that the IAM role has the correct permissions
- Verify the S3 bucket name is correct
- Ensure the IAM role trust policy allows your GitHub repository

### CloudFront invalidation taking too long

- CloudFront invalidations typically take 5-15 minutes
- The workflow will wait up to 5 minutes, then continue
- Check CloudFront console for invalidation status

### Changes not appearing on website

- Wait 1-2 minutes for CloudFront propagation
- Check CloudFront invalidation status
- Verify files were uploaded to S3 correctly
- Clear browser cache or test in incognito mode

## Security

✅ Uses OIDC authentication (no access keys stored)  
✅ IAM role restricted to specific repository and branch  
✅ Least privilege permissions (only S3 and CloudFront access)  
✅ No sensitive data in workflow files

## Alternative Deployment (Apache/EC2)

For deploying to Apache servers or AWS EC2:

1. Build the static site: `npm run build`
2. Upload the `out/` directory contents to your web server
3. Ensure `.htaccess` file is in the root directory
4. Configure Apache with `mod_rewrite` enabled
