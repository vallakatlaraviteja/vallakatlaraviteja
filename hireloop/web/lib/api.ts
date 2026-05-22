/**
 * Thin fetch wrapper around the hireloop API.
 * Single-user mode — relies on the session cookie set by /api/auth/login.
 */

const BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export class ApiError extends Error {
  constructor(public status: number, message: string, public body?: unknown) {
    super(message);
  }
}

export async function api<T>(path: string, init: RequestInit = {}): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    ...init,
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(init.headers ?? {}),
    },
  });
  if (!res.ok) {
    let body: unknown = undefined;
    try {
      body = await res.json();
    } catch {
      /* ignore */
    }
    throw new ApiError(res.status, `${res.status} ${res.statusText}`, body);
  }
  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}

export type Job = {
  id: string;
  company: string;
  title: string;
  location: string | null;
  remote: boolean;
  url: string | null;
  status: string;
  match_score: number | null;
  description_md: string;
  created_at: string;
};

export const Jobs = {
  list: () => api<Job[]>("/api/jobs"),
  create: (input: { url?: string; company?: string; title?: string; description_md?: string }) =>
    api<Job>("/api/jobs", { method: "POST", body: JSON.stringify(input) }),
  archive: (id: string) => api<Job>(`/api/jobs/${id}/archive`, { method: "POST" }),
};

export const Auth = {
  login: (email: string) => api<{ email: string }>("/api/auth/login", { method: "POST", body: JSON.stringify({ email }) }),
  logout: () => api<{ status: string }>("/api/auth/logout", { method: "POST" }),
  me: () => api<{ email: string }>("/api/auth/me"),
};
