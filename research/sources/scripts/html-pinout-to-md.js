const fs = require('fs');
const path = require('path');

const inFile = process.argv[2];
const outFile = process.argv[3];
const title = process.argv[4] || 'WDS pinout extract';

const html = fs.readFileSync(inFile, 'utf8');
const re =
  /<tr class="pinrow1"><td>(\d+|[^<]*)<\/td><td>([^<]*)<\/td><td>([^<]*)<\/td><td>([^<]*)<\/td><\/tr>/g;

const sections = html.split('<h2>').slice(1);
let md = `# ${title}\n\n`;
for (const chunk of sections) {
  const titleMatch = chunk.match(/^([^<]+)<\/h2>/);
  if (!titleMatch) continue;
  const sectionTitle = titleMatch[1].trim();
  const body = chunk.split('</h2>')[1] || '';
  const rows = [];
  let m;
  while ((m = re.exec(body)) !== null) {
    rows.push(`| ${m[1]} | ${m[2].trim()} | ${m[3].trim()} | ${m[4].trim()} |`);
  }
  if (rows.length === 0) continue;
  md += `## ${sectionTitle}\n\n| Pin | Type | Signal | Connection |\n|---:|---|---|---|\n${rows.join('\n')}\n\n`;
}

fs.mkdirSync(path.dirname(outFile), { recursive: true });
fs.writeFileSync(outFile, md);
console.log('Wrote', outFile, md.length, 'chars');
