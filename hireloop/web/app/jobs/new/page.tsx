"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Jobs } from "@/lib/api";

export default function NewJob() {
  const router = useRouter();
  const [url, setUrl] = useState("");
  const [pasting, setPasting] = useState(false);
  const [company, setCompany] = useState("");
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    try {
      const payload = pasting
        ? { company, title, description_md: description }
        : { url };
      await Jobs.create(payload);
      router.push("/");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main className="mx-auto max-w-2xl p-8">
      <h1 className="mb-6 text-xl font-semibold">Add a job</h1>
      <div className="mb-4 flex gap-3 text-sm">
        <button
          onClick={() => setPasting(false)}
          className={`rounded-md px-3 py-1 ${!pasting ? "bg-accent-600" : "bg-ink-100/10"}`}
        >
          From URL
        </button>
        <button
          onClick={() => setPasting(true)}
          className={`rounded-md px-3 py-1 ${pasting ? "bg-accent-600" : "bg-ink-100/10"}`}
        >
          Paste manually
        </button>
      </div>
      <form className="flex flex-col gap-3" onSubmit={submit}>
        {pasting ? (
          <>
            <input className="input" placeholder="Company" value={company} onChange={(e) => setCompany(e.target.value)} required />
            <input className="input" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} required />
            <textarea className="input min-h-[200px]" placeholder="Job description (Markdown OK)" value={description} onChange={(e) => setDescription(e.target.value)} required />
          </>
        ) : (
          <input className="input" placeholder="https://boards.greenhouse.io/..." value={url} onChange={(e) => setUrl(e.target.value)} required />
        )}
        {error && <p className="text-sm text-red-400">{error}</p>}
        <button
          type="submit"
          disabled={submitting}
          className="rounded-md bg-accent-600 px-3 py-2 text-sm font-medium hover:bg-accent-500 disabled:opacity-60"
        >
          {submitting ? "Adding…" : "Add"}
        </button>
      </form>
      <style jsx global>{`
        .input {
          @apply rounded-md border border-ink-100/10 bg-ink-950 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-accent-600;
        }
      `}</style>
    </main>
  );
}
