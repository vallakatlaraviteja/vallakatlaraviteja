"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";
import { Auth, Jobs } from "@/lib/api";
import { useState } from "react";

export default function Home() {
  const [email, setEmail] = useState("");
  const me = useQuery({ queryKey: ["me"], queryFn: Auth.me, retry: false });
  const jobs = useQuery({ queryKey: ["jobs"], queryFn: Jobs.list, enabled: me.isSuccess });

  if (me.isLoading) return <Centered>Loading…</Centered>;
  if (me.isError) {
    return (
      <Centered>
        <form
          className="flex w-80 flex-col gap-3 rounded-xl border border-ink-100/10 bg-ink-900 p-6"
          onSubmit={async (e) => {
            e.preventDefault();
            await Auth.login(email);
            window.location.reload();
          }}
        >
          <h1 className="text-lg font-medium">hireloop</h1>
          <p className="text-sm text-ink-50/60">Single-owner sign in.</p>
          <input
            type="email"
            placeholder="owner email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="rounded-md border border-ink-100/10 bg-ink-950 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-accent-600"
            required
          />
          <button className="rounded-md bg-accent-600 px-3 py-2 text-sm font-medium hover:bg-accent-500">
            Continue
          </button>
        </form>
      </Centered>
    );
  }

  return (
    <main className="mx-auto max-w-4xl p-8">
      <header className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">hireloop</h1>
          <p className="text-sm text-ink-50/60">{me.data?.email}</p>
        </div>
        <Link href="/jobs/new" className="rounded-md bg-accent-600 px-3 py-2 text-sm font-medium hover:bg-accent-500">
          + Add job
        </Link>
      </header>

      <section>
        <h2 className="mb-4 text-sm uppercase tracking-wide text-ink-50/60">Pipeline</h2>
        {jobs.isLoading && <p className="text-sm text-ink-50/60">Loading jobs…</p>}
        {jobs.data?.length === 0 && (
          <p className="text-sm text-ink-50/60">
            No jobs yet. Paste a JD URL on{" "}
            <Link className="text-accent-500" href="/jobs/new">
              the add-job page
            </Link>{" "}
            to get started.
          </p>
        )}
        <ul className="divide-y divide-ink-100/10">
          {jobs.data?.map((j) => (
            <li key={j.id} className="flex items-center justify-between py-3">
              <div>
                <div className="font-medium">{j.title}</div>
                <div className="text-xs text-ink-50/60">
                  {j.company} · {j.location ?? "—"} · {j.remote ? "remote" : "onsite"}
                </div>
              </div>
              <span className="rounded-full bg-ink-100/10 px-2 py-0.5 text-xs">{j.status}</span>
            </li>
          ))}
        </ul>
      </section>
    </main>
  );
}

function Centered({ children }: { children: React.ReactNode }) {
  return <div className="flex min-h-screen items-center justify-center">{children}</div>;
}
