#!/usr/bin/env python3
"""Capturas auditáveis do frontend ServiPlus AS-IS; não prova conformidade ConecTA.

Run from a local machine with original frontend serving port 3000:
  pip install playwright && python -m playwright install chromium
  python capture_frontend_m08.py --frontend-dir /path/freelance-frontend
"""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

PINNED = "f41d72e8ace6c716e799131cb46ce425a1a4c215"

CASES = [
 ("5.13a", "/#/login", "Aceder à sua conta", None, "login de demonstração"),
 ("5.13b", "/#/register", "Registe uma nova conta", None, "role único"),
 ("5.14", "/#/offers", "Pesquisar", None, "oportunidades mock/localStorage"),
 ("5.15", "/#/profile/1", "Carlos Tembe", None, "perfil mock"),
 ("5.16", "/#/offers/1", "Submeter a sua Proposta Comercial", "charlie@gmail.com", "proposta simulada"),
 ("5.17", "/#/dashboard", "Contratos & Estágio", "vagas@maputodigital.co.mz", "sem AgreementVersion"),
 ("5.18", "/#/profile/1", "Avaliações dos Contratantes", None, "reputação simulada"),
 ("5.19", "/#/dashboard", "Moderação de BI", "admin@serviplus.co.mz", "sem DisputeEvidence / WAITING_INFORMATION")
]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--frontend-dir", required=True, type=Path)
    p.add_argument("--url", default="http://127.0.0.1:3000")
    p.add_argument("--output", type=Path, default=Path("evidencias-m08"))
    p.add_argument("--expected-sha", default=PINNED)
    p.add_argument("--allow-different-revision", action="store_true")
    args=p.parse_args()
    u=urlparse(args.url)
    if u.scheme not in ("http","https") or u.hostname not in ("localhost","127.0.0.1","::1"):
        p.error("Servidor tem de estar em localhost.")
    if not (args.frontend_dir/"src/App.tsx").exists():
        p.error("Frontend não encontrado.")
    sha=subprocess.check_output(["git","-C",str(args.frontend_dir),"rev-parse","HEAD"],text=True).strip()
    if sha!=args.expected_sha and not args.allow_different_revision:
        p.error("Revisão diferente da auditada: "+sha)
    from playwright.sync_api import sync_playwright
    args.output.mkdir(parents=True,exist_ok=True)
    result={"collected_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "frontend_sha":sha,"matches_pin":sha==args.expected_sha,
            "base_url":args.url,"browser":"Playwright Chromium 1365x900",
            "source":"frontend mockApi/localStorage; sem ligação comprovada à API",
            "cases":[]}
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        try:
            for id,route,text,account,limit in CASES:
                context=browser.new_context(viewport={"width":1365,"height":900},locale="pt-PT")
                page=context.new_page()
                item={"id":id,"route":route,"limitation":limit}
                try:
                    page.goto(args.url.rstrip("/")+("/#/login" if account else route),
                              wait_until="domcontentloaded",timeout=30000)
                    if account:
                        page.get_by_text(account,exact=True).first.click(timeout=15000)
                        page.wait_for_url("**/#/dashboard",timeout=15000)
                        page.goto(args.url.rstrip("/")+route,wait_until="domcontentloaded")
                    page.get_by_text(text,exact=False).first.wait_for(timeout=15000)
                    if id=="5.17":
                        page.get_by_role("button",name="Contratos & Estágio").first.click(timeout=10000)
                    if id=="5.19":
                        page.get_by_role("button",name="Moderação de BI").first.click(timeout=10000)
                    target=args.output/("figura_"+id.replace(".","_")+".png")
                    page.screenshot(path=str(target),full_page=True,animations="disabled")
                    item.update(status=("CAPTURA_MOCK_NAO_EQUIVALENTE" if id in ("5.17","5.19") else
                                        "CAPTURA_REAL_DA_INTERFACE_SIMULADA"),
                                filename=target.name,
                                sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                                url=page.url)
                except Exception as e:
                    item.update(status="NAO_CAPTURADO",error=str(e).split("\n")[0][:280])
                result["cases"].append(item)
                context.close()
        finally:
            browser.close()
    (args.output/"manifesto_m08.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"manifesto":str(args.output/"manifesto_m08.json"),
                      "capturas":sum(x["status"]!="NAO_CAPTURADO" for x in result["cases"]),
                      "cenarios":len(result["cases"])},ensure_ascii=False))
if __name__=="__main__":
    main()
