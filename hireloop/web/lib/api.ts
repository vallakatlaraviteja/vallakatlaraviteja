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

export type ApplicationStatus =
  | "saved"
  | "tailoring"
  | "ready_to_apply"
  | "applied"
  | "recruiter_screen"
  | "tech_screen"
  | "onsite"
  | "offer"
  | "accepted"
  | "rejected"
  | "withdrawn";

export type Application = {
  id: string;
  candidate_id: string;
  job_id: string;
  status: ApplicationStatus;
  applied_at: string | null;
  next_action: string | null;
  next_action_due: string | null;
  referrer_name: string | null;
  referrer_email: string | null;
  notes_md: string | null;
  created_at: string;
  updated_at: string;
  job: Job;
};



export type Funnel = {
  active_by_stage: { stage: ApplicationStatus; count: number }[];
  reached_by_stage: { stage: ApplicationStatus; count: number }[];
  apps_submitted: number;
  recruiter_screens: number;
  tech_screens: number;
  onsites: number;
  offers: number;
  accepted: number;
  app_to_screen_rate: number;
  screen_to_tech_rate: number;
  tech_to_onsite_rate: number;
  onsite_to_offer_rate: number;
};

export const Jobs = {
  list: () => api<Job[]>("/api/jobs"),
  create: (input: { url?: string; company?: string; title?: string; description_md?: string }) =>
    api<Job>("/api/jobs", { method: "POST", body: JSON.stringify(input) }),
  archive: (id: string) => api<Job>(`/api/jobs/${id}/archive`, { method: "POST" }),
};

export const Applications = {
  list: () => api<Application[]>("/api/applications"),
  create: (input: { job_id: string; notes_md?: string; referrer_name?: string; referrer_email?: string }) =>
    api<Application>("/api/applications", { method: "POST", body: JSON.stringify(input) }),
  setStatus: (id: string, status: ApplicationStatus) =>
    api<Application>(`/api/applications/${id}`, { method: "PATCH", body: JSON.stringify({ status }) }),
  update: (id: string, patch: Partial<Pick<Application, "next_action" | "notes_md" | "referrer_name" | "referrer_email">>) =>
    api<Application>(`/api/applications/${id}`, { method: "PATCH", body: JSON.stringify(patch) }),
};

export const Analytics = {
  funnel: () => api<Funnel>("/api/analytics/funnel"),
};

export const Auth = {
  login: (email: string) => api<{ email: string }>("/api/auth/login", { method: "POST", body: JSON.stringify({ email }) }),
  logout: () => api<{ status: string }>("/api/auth/logout", { method: "POST" }),
  me: () => api<{ email: string }>("/api/auth/me"),
};
