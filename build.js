const fs = require("fs");
const path = require("path");
const CleanCSS = require("clean-css");
const UglifyJS = require("uglify-js");

const buildDir = path.join(__dirname, "build");
const assetsBuildDir = path.join(buildDir, "assets");
const cssBuildDir = path.join(assetsBuildDir, "css");
const jsBuildDir = path.join(assetsBuildDir, "js");
const imagesBuildDir = path.join(assetsBuildDir, "images");

// Create build directory structure
const createDirStructure = () => {
  [buildDir, assetsBuildDir, cssBuildDir, jsBuildDir, imagesBuildDir].forEach(
    (dir) => {
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
    },
  );
};

console.log("🏗️  Setting up build directory structure...\n");
createDirStructure();

// Bundle and minify CSS
console.log("📦 Bundling and minifying CSS files...");
const cssDir = path.join(__dirname, "assets/css");
const cssFiles = [
  "bootstrap.min.css",
  "animate.css",
  "lineicons.css",
  "main.css",
  "accessibility.css",
];
let cssBundle = "";

cssFiles.forEach((file) => {
  const filePath = path.join(cssDir, file);
  if (fs.existsSync(filePath)) {
    const content = fs.readFileSync(filePath, "utf8");
    cssBundle += `/* ${file} */\n${content}\n`;
  }
});

const minifiedCSS = new CleanCSS().minify(cssBundle).styles;
const bundleCSSPath = path.join(cssBuildDir, "bundle.min.css");
fs.writeFileSync(bundleCSSPath, minifiedCSS);

const originalCSSSize = (cssBundle.length / 1024).toFixed(2);
const minCSSSize = (minifiedCSS.length / 1024).toFixed(2);
const cssReduction = (
  ((cssBundle.length - minifiedCSS.length) / cssBundle.length) *
  100
).toFixed(1);

console.log(`  ✓ CSS bundle created: build/assets/css/bundle.min.css`);
console.log(
  `    Original: ${originalCSSSize}KB → Minified: ${minCSSSize}KB (${cssReduction}% reduction)\n`,
);

// Bundle and minify JS
console.log("📦 Bundling and minifying JavaScript files...");
const jsDir = path.join(__dirname, "assets/js");
const jsFiles = [
  "bootstrap.bundle.min.js",
  "wow.min.js",
  "translations.js",
  "language.js",
  "main.js",
];
let jsBundle = "";

jsFiles.forEach((file) => {
  const filePath = path.join(jsDir, file);
  if (fs.existsSync(filePath)) {
    const content = fs.readFileSync(filePath, "utf8");
    jsBundle += `/* ${file} */\n${content}\n`;
  }
});

const minifiedJS = UglifyJS.minify(jsBundle);
if (minifiedJS.error) {
  console.error("  ✗ Error minifying JS:", minifiedJS.error);
  process.exit(1);
} else {
  const bundleJSPath = path.join(jsBuildDir, "bundle.min.js");
  fs.writeFileSync(bundleJSPath, minifiedJS.code);

  const originalJSSize = (jsBundle.length / 1024).toFixed(2);
  const minJSSize = (minifiedJS.code.length / 1024).toFixed(2);
  const jsReduction = (
    ((jsBundle.length - minifiedJS.code.length) / jsBundle.length) *
    100
  ).toFixed(1);

  console.log(`  ✓ JS bundle created: build/assets/js/bundle.min.js`);
  console.log(
    `    Original: ${originalJSSize}KB → Minified: ${minJSSize}KB (${jsReduction}% reduction)\n`,
  );
}

// Minify HTML files
const minifyHTML = (filePath, outputPath) => {
  let htmlContent = fs.readFileSync(filePath, "utf8");

  // Replace all individual CSS files with single bundle
  const cssBlockRegex =
    /<!-- CSS Files.*?-->\s*(?:<link rel="stylesheet" href="assets\/css\/[^"]+"\s*\/>[\s\n]*)+/gs;
  htmlContent = htmlContent.replace(
    cssBlockRegex,
    '<!-- CSS Bundle (Minified & Optimized) -->\n  <link rel="stylesheet" href="assets/css/bundle.min.css">\n  ',
  );

  // Replace all individual JS files with single bundle
  const jsBlockRegex =
    /<!-- ====== All Javascript Files ====== -->[\s\S]*?(?:<script src="assets\/js\/[^"]+"><\/script>[\s\n]*)+/;
  htmlContent = htmlContent.replace(
    jsBlockRegex,
    '<!-- ====== All Javascript Files ====== -->\n  <!-- JavaScript Bundle (Minified & Optimized) -->\n  <script src="assets/js/bundle.min.js"></script>\n  ',
  );

  // Remove comments but keep important ones
  htmlContent = htmlContent.replace(/<!--[\s\S]*?-->/g, (match) => {
    if (match.includes("!--")) return match; // Keep IE conditional comments
    return "";
  });

  // Minify: remove extra whitespace and newlines
  htmlContent = htmlContent
    .replace(/\s{2,}/g, " ")
    .replace(/>\s+</g, "><")
    .trim();

  fs.writeFileSync(outputPath, htmlContent);

  const originalSize = (
    fs.readFileSync(filePath, "utf8").length / 1024
  ).toFixed(2);
  const minSize = (htmlContent.length / 1024).toFixed(2);
  const reduction = (
    ((fs.readFileSync(filePath, "utf8").length - htmlContent.length) /
      fs.readFileSync(filePath, "utf8").length) *
    100
  ).toFixed(1);

  return { originalSize, minSize, reduction };
};

console.log("📝 Minifying HTML pages...");

// Minify index.html
const indexStats = minifyHTML(
  path.join(__dirname, "index.html"),
  path.join(buildDir, "index.html"),
);
console.log(`  ✓ index.html minified`);
console.log(
  `    Original: ${indexStats.originalSize}KB → Minified: ${indexStats.minSize}KB (${indexStats.reduction}% reduction)`,
);

// Minify careers.html if it exists
const careersPath = path.join(__dirname, "careers.html");
if (fs.existsSync(careersPath)) {
  const careersStats = minifyHTML(
    careersPath,
    path.join(buildDir, "careers.html"),
  );
  console.log(`  ✓ careers.html minified`);
  console.log(
    `    Original: ${careersStats.originalSize}KB → Minified: ${careersStats.minSize}KB (${careersStats.reduction}% reduction)`,
  );
} else {
  console.log(`  ⓘ careers.html not found (skipped)`);
}
console.log();

// Copy SVG files and other images
const copyFilesRecursive = (src, dest) => {
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
  const files = fs.readdirSync(src);
  files.forEach((file) => {
    const srcPath = path.join(src, file);
    const destPath = path.join(dest, file);
    if (fs.lstatSync(srcPath).isDirectory()) {
      copyFilesRecursive(srcPath, destPath);
    } else if (file.endsWith(".svg") || file.endsWith(".webp")) {
      fs.copyFileSync(srcPath, destPath);
    }
  });
};

console.log("🖼️  Copying optimized images...");
const imgDir = path.join(__dirname, "assets/images");
copyFilesRecursive(imgDir, imagesBuildDir);
console.log(`  ✓ Images copied to build/assets/images/\n`);

// Copy fonts and other static assets
console.log("📁 Copying static assets...");
const fontsDir = path.join(__dirname, "assets/fonts");
const fontsBuildDir = path.join(assetsBuildDir, "fonts");
if (fs.existsSync(fontsDir)) {
  fs.cpSync(fontsDir, fontsBuildDir, { recursive: true });
  console.log(`  ✓ Fonts copied`);
}

// Copy root static files
const staticFiles = ["robots.txt", "sitemap.xml", "humans.txt"];
staticFiles.forEach((file) => {
  const srcPath = path.join(__dirname, file);
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, path.join(buildDir, file));
  }
});
console.log(`  ✓ Static files copied\n`);

// Summary
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log("✅ BUILD PROCESS COMPLETE!\n");
console.log("📂 Build folder structure:");
console.log("   build/");
console.log("   ├── index.html (minified)");
console.log("   ├── careers.html (minified)");
console.log("   ├── robots.txt");
console.log("   ├── sitemap.xml");
console.log("   ├── humans.txt");
console.log("   └── assets/");
console.log("       ├── css/bundle.min.css");
console.log("       ├── js/bundle.min.js");
console.log("       ├── images/ (optimized)");
console.log("       └── fonts/");
console.log(
  "\n🚀 Ready for deployment! Upload the build/ folder to your server.\n",
);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
