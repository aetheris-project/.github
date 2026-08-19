<p align="center">
  <img src="https://raw.githubusercontent.com/aetheris-project/.github/main/assets/logo.svg" alt="Aetheris Enterprise Platform" width="420">
</p>

<h3 align="center">Enterprise billing and virtualization management</h3>

<p align="center">
  <strong>One control plane for billing, panels and hypervisors.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/TypeScript-5.6-blue?logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Next.js-14-black?logo=next.js&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/Prisma-5-2D3748?logo=prisma&logoColor=white" alt="Prisma">
  <img src="https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Redis-7-DC382D?logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Tailwind-3.4-06B6D4?logo=tailwindcss&logoColor=white" alt="Tailwind">
  <img src="https://img.shields.io/badge/Nextra-2-000000?logo=next.js&logoColor=white" alt="Nextra">
</p>

---

## Mission

Aetheris converges WHMCS, FOSSBilling, Pterodactyl Panel, Proxmox VE and
VirtFusion into a single enterprise control plane: one billing engine, one
client portal, one set of hypervisor drivers and one admin surface, with
dynamic whitelabeling and a theme system that runs across every surface of
the platform.

We build with strict-mode TypeScript, token-driven design, zero layout
shifts, SSR-first rendering and an English-only, emoji-free standard across
code, UI and documentation.

## Repositories

| Repository | Description | Stack |
| --- | --- | --- |
| [aetheris-app](https://github.com/aetheris-project/aetheris-app) | Core billing system, admin control plane, hypervisor drivers (Pterodactyl, Proxmox VE, VirtFusion) and client portal. Includes a self-contained Python REST backend. | Next.js 14, TypeScript, Prisma, PostgreSQL, Redis, BullMQ, Python, FastAPI |
| [aetheris-website](https://github.com/aetheris-project/aetheris-website) | Marketing site, interactive product demo, dynamic SEO and landing page. | Next.js 14, Tailwind CSS, `@vercel/og` |
| [aetheris-docs](https://github.com/aetheris-project/aetheris-docs) | Wiki, per-OS installation guides, developer SDK and OpenAPI specifications. | Nextra 2 |
| [aetheris-installer](https://github.com/aetheris-project/aetheris-installer) | Automated cross-platform installer: archinstall-style TUI wizard plus non-interactive `--yes` mode with native systemd, launchd and Windows service generation. | Python 3.10+ |

### Feature highlights

- Unified billing engine: invoices, subscriptions, proration, dunning and
  tax, wired to Stripe, PayPal and Mollie.
- Universal hypervisor driver contract with native Pterodactyl (Application
  and Client API), Proxmox VE API v2, VirtFusion REST, cPanel/WHM and
  DirectAdmin backends.
- Client portal with server lifecycle, VNC console (WebSocket token
  issuance), backups and payment methods.
- Admin control plane: node management, allocation pools, nest and egg
  targeting, backup policies and per-client resource limits.
- Dynamic whitelabeling: brand, accent colors, navigation and email
  templates configured at runtime; dark / light / system themes persisted
  per visitor.
- Background orchestration with BullMQ: provisioning, billing runs,
  telemetry and email delivery.
- Self-contained Python backend (FastAPI + SQLite) for demos and development,
  plus a fully automated installer for Linux, macOS and Windows.

## Getting started

```bash
# Automated install on any OS (wizard or non-interactive)
git clone https://github.com/aetheris-project/aetheris-installer.git
cd aetheris-installer
python -m aetheris_installer --yes

# Or run the platform in development
git clone https://github.com/aetheris-project/aetheris-app.git
cd aetheris-app && npm install && npx prisma migrate dev && npm run dev
```

Full guidance lives in the [documentation wiki](https://github.com/aetheris-project/aetheris-docs)
and the [interactive demo](https://github.com/aetheris-project/aetheris-website).

## Contributing

We welcome contributions across all repositories. Please follow these
standards:

- Strict-mode TypeScript; run `npm run typecheck` before opening a pull
  request.
- Token-driven design: use the CSS-variable tokens (`bg-surface`,
  `border-edge`, `text-muted`, accents) instead of hardcoded colors.
- Zero layout shifts: reserve layout space for loading states and toasts.
- English only across code, UI, commit messages and documentation; no
  emojis.
- Document API changes in the wiki and keep the OpenAPI specification in
  sync.
- The installer repository is emoji-free by design and writes only inside
  its target directory.

Open a pull request on the relevant repository. For larger changes, open an
issue first to align on the approach.

## Contact

- Documentation: [aetheris-docs](https://github.com/aetheris-project/aetheris-docs)
- Interactive demo: [aetheris-website](https://github.com/aetheris-project/aetheris-website)
- Support: `ops@aetheris.enterprise`
