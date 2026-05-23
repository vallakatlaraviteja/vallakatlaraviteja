"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import Link from "next/link";
import { Applications, Analytics, Application, ApplicationStatus, Funnel } from "@/lib/api";

const STAGES: { key: ApplicationStatus; label: string }[] = [
  { key: "saved", label: "Saved" },
  { key: "tailoring", label: "Tailoring" },
  { key: "ready_to_apply", label: "Ready" },
  { key: "applied", label: "Applied" },
  { key: "recruiter_screen", label: "Recruiter" },
  { key: "tech_screen", label: "Tech" },
  { key: "onsite", label: "Onsite" },
  { key: "offer", label: "Offer" },
];

const TERMINAL: ApplicationStatus[] = ["accepted", "rejected", "withdrawn"];

export default function PipelinePage() {
  const apps = useQuery({ queryKey: ["applications"], queryFn: Applications.list });
  const funnel = useQuery({ queryKey: ["funnel"], queryFn: Analytics.funnel });

  return (
    <main className="mx-auto max-w-7xl p-6">
      <header className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-xl font-semibold">Pipeline</h1>
          <p className="text-xs text-ink-50/60">
            <Link className="text-accent-500" href="/">Home</Link>
            {" · "}
            <Link className="text-accent-500" href="/jobs/new">+ Add job</Link>
          </p>
        </div>
        {funnel.data && <FunnelBar data={funnel.data} />}
      </header>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-8">
        {STAGES.map((stage) => (
          <Column
            key={stage.key}
            stage={stage}
            apps={(apps.data ?? []).filter((a) => a.status === stage.key)}
          />
        ))}
      </div>
    </main>
  );
}



function FunnelBar({ data }: { data: Funnel }) {
  const fmt = (n: number) => `${(n * 100).toFixed(0)}%`;
  return (
    <div className="text-right text-xs leading-relaxed text-ink-50/70">
      <div>
        apps {data.apps_submitted} · screens {data.recruiter_screens} · tech {data.tech_screens} · onsite {data.onsites} · offers {data.offers}
      </div>
      <div className="text-ink-50/50">
        {fmt(data.app_to_screen_rate)} → {fmt(data.screen_to_tech_rate)} → {fmt(data.tech_to_onsite_rate)} → {fmt(data.onsite_to_offer_rate)}
      </div>
    </div>
  );
}

function Column({
  stage,
  apps,
}: {
  stage: { key: ApplicationStatus; label: string };
  apps: Application[];
}) {
  return (
    <section className="rounded-lg border border-ink-100/10 bg-ink-900/40 p-3">
      <header className="mb-2 flex items-center justify-between text-xs uppercase tracking-wide text-ink-50/60">
        <span>{stage.label}</span>
        <span className="rounded-full bg-ink-100/10 px-1.5 py-0.5">{apps.length}</span>
      </header>
      <ul className="flex flex-col gap-2">
        {apps.map((app) => (
          <Card key={app.id} app={app} />
        ))}
      </ul>
    </section>
  );
}



function Card({ app }: { app: Application }) {
  const qc = useQueryClient();
  const move = useMutation({
    mutationFn: (next: ApplicationStatus) => Applications.setStatus(app.id, next),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["applications"] });
      qc.invalidateQueries({ queryKey: ["funnel"] });
    },
  });

  const next = NEXT_STAGE[app.status];

  return (
    <li className="rounded-md border border-ink-100/10 bg-ink-950 p-3 text-sm">
      <div className="font-medium leading-tight">{app.job.title}</div>
      <div className="mt-0.5 text-xs text-ink-50/60">{app.job.company}</div>
      <div className="mt-2 flex items-center gap-2">
        {next && (
          <button
            onClick={() => move.mutate(next)}
            disabled={move.isPending}
            className="rounded bg-accent-600 px-2 py-0.5 text-xs hover:bg-accent-500 disabled:opacity-50"
          >
            → {next.replace("_", " ")}
          </button>
        )}
        {!TERMINAL.includes(app.status) && (
          <button
            onClick={() => move.mutate("rejected")}
            disabled={move.isPending}
            className="rounded border border-ink-100/10 px-2 py-0.5 text-xs text-ink-50/60 hover:bg-ink-100/5"
          >
            ✗
          </button>
        )}
      </div>
    </li>
  );
}

const NEXT_STAGE: Partial<Record<ApplicationStatus, ApplicationStatus>> = {
  saved: "applied",
  tailoring: "applied",
  ready_to_apply: "applied",
  applied: "recruiter_screen",
  recruiter_screen: "tech_screen",
  tech_screen: "onsite",
  onsite: "offer",
  offer: "accepted",
};
