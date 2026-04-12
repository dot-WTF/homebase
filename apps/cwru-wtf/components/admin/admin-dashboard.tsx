'use client';

import { type ReactNode, useDeferredValue, useState } from 'react';
import { signOut } from 'next-auth/react';
import {
  ArrowUpRight,
  CheckCheck,
  Clock3,
  LoaderCircle,
  type LucideIcon,
  LogOut,
  Mail,
  Phone,
  RefreshCw,
  Search,
  ShieldCheck,
  Sparkles,
  Video,
  XCircle,
} from 'lucide-react';
import { toast } from 'sonner';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

export interface AdminSubmission {
  id: number;
  name: string;
  email: string;
  categories?: string;
  otherCategory?: string | null;
  wtfIdea?: string;
  currentProject?: string;
  youtubeLink?: string;
  whatsapp?: string | null;
  interests?: string | null;
  isApproved: boolean | null;
  createdAt: string;
  updatedAt: string;
}

interface AdminDashboardProps {
  admin: {
    email: string;
    name: string;
    role: string;
  };
  initialSubmissions: AdminSubmission[];
}

type SubmissionFilter = 'all' | 'pending' | 'approved' | 'rejected';

const dateFormatter = new Intl.DateTimeFormat('en-US', {
  dateStyle: 'medium',
  timeStyle: 'short',
});

const statusCopy = {
  approved: {
    badgeClassName:
      'border-emerald-400/20 bg-emerald-400/12 text-emerald-100',
    cardClassName:
      'border-white/10 bg-slate-950/70 shadow-[0_24px_80px_-36px_rgba(16,185,129,0.65)]',
    icon: CheckCheck,
    label: 'Approved',
    metricClassName: 'text-emerald-200',
  },
  pending: {
    badgeClassName: 'border-cyan-400/20 bg-cyan-400/12 text-cyan-100',
    cardClassName:
      'border-cyan-400/20 bg-slate-950/80 shadow-[0_30px_90px_-38px_rgba(34,211,238,0.7)]',
    icon: Clock3,
    label: 'Pending',
    metricClassName: 'text-cyan-200',
  },
  rejected: {
    badgeClassName: 'border-rose-400/20 bg-rose-400/12 text-rose-100',
    cardClassName:
      'border-white/10 bg-slate-950/70 shadow-[0_24px_80px_-36px_rgba(244,63,94,0.5)]',
    icon: XCircle,
    label: 'Rejected',
    metricClassName: 'text-rose-200',
  },
} as const;

export default function AdminDashboard({
  admin,
  initialSubmissions,
}: AdminDashboardProps) {
  const [submissions, setSubmissions] =
    useState<AdminSubmission[]>(initialSubmissions);
  const [filter, setFilter] = useState<SubmissionFilter>('all');
  const [search, setSearch] = useState('');
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [updatingId, setUpdatingId] = useState<number | null>(null);
  const deferredSearch = useDeferredValue(search.trim().toLowerCase());

  const stats = getSubmissionStats(submissions);
  const filterOptions = [
    { id: 'all', label: 'All', count: stats.total },
    { id: 'pending', label: 'Pending', count: stats.pending },
    { id: 'approved', label: 'Approved', count: stats.approved },
    { id: 'rejected', label: 'Rejected', count: stats.rejected },
  ] as const satisfies ReadonlyArray<{
    id: SubmissionFilter;
    label: string;
    count: number;
  }>;

  const filteredSubmissions = submissions.filter((submission) => {
    if (filter === 'pending' && submission.isApproved !== null) {
      return false;
    }

    if (filter === 'approved' && submission.isApproved !== true) {
      return false;
    }

    if (filter === 'rejected' && submission.isApproved !== false) {
      return false;
    }

    if (!deferredSearch) {
      return true;
    }

    return buildSearchBlob(submission).includes(deferredSearch);
  });

  const refreshSubmissions = async () => {
    setIsRefreshing(true);

    try {
      const response = await fetch('/api/admin/submissions', {
        cache: 'no-store',
      });

      if (!response.ok) {
        throw new Error('Failed to fetch submissions');
      }

      const refreshedSubmissions =
        (await response.json()) as AdminSubmission[];

      setSubmissions(refreshedSubmissions);
      toast.success('Admin dashboard refreshed.');
    } catch (error) {
      console.error('Refresh error:', error);
      toast.error('Unable to refresh submissions right now.');
    } finally {
      setIsRefreshing(false);
    }
  };

  const updateSubmissionStatus = async (
    submissionId: number,
    isApproved: boolean
  ) => {
    setUpdatingId(submissionId);

    try {
      const response = await fetch('/api/admin/submissions', {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: submissionId, isApproved }),
      });

      if (!response.ok) {
        throw new Error('Failed to update submission');
      }

      const updatedSubmission = (await response.json()) as AdminSubmission;

      setSubmissions((currentSubmissions) =>
        currentSubmissions.map((submission) =>
          submission.id === submissionId ? updatedSubmission : submission
        )
      );

      toast.success(
        `Submission ${isApproved ? 'approved' : 'rejected'} successfully.`
      );
    } catch (error) {
      console.error('Update error:', error);
      toast.error('We could not update that submission.');
    } finally {
      setUpdatingId(null);
    }
  };

  return (
    <div className="min-h-screen overflow-hidden bg-[#07131f] text-slate-50">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.22),_transparent_24%),radial-gradient(circle_at_top_right,_rgba(45,212,191,0.18),_transparent_28%),linear-gradient(180deg,_#07131f_0%,_#020617_100%)]" />
        <div className="absolute left-[-8rem] top-20 h-72 w-72 rounded-full bg-cyan-400/12 blur-3xl" />
        <div className="absolute right-[-5rem] top-[-3rem] h-80 w-80 rounded-full bg-teal-300/10 blur-3xl" />
        <div className="absolute inset-0 opacity-30 [background-image:linear-gradient(to_right,rgba(148,163,184,0.08)_1px,transparent_1px),linear-gradient(to_bottom,rgba(148,163,184,0.08)_1px,transparent_1px)] [background-size:72px_72px] [mask-image:radial-gradient(circle_at_center,black,transparent_80%)]" />
      </div>

      <main className="relative mx-auto flex w-full max-w-7xl flex-col gap-6 px-4 py-6 sm:px-6 lg:px-8 lg:py-10">
        <section className="overflow-hidden rounded-[32px] border border-white/10 bg-white/5 p-6 shadow-[0_40px_140px_-48px_rgba(8,47,73,0.95)] backdrop-blur-xl sm:p-8">
          <div className="flex flex-col gap-8 xl:flex-row xl:items-start xl:justify-between">
            <div className="max-w-3xl">
              <div className="inline-flex items-center gap-2 rounded-full border border-cyan-300/20 bg-cyan-300/10 px-3 py-1 text-xs font-medium uppercase tracking-[0.28em] text-cyan-100/90">
                <Sparkles className="h-3.5 w-3.5" />
                Admin Console
              </div>

              <h1 className="mt-5 font-serif text-4xl leading-tight text-white sm:text-5xl">
                Review submissions with a cleaner, faster control room.
              </h1>

              <p className="mt-4 max-w-2xl text-sm leading-6 text-slate-300 sm:text-base">
                Premium layout, calmer colors, and faster moderation tools for
                the team running CWRU.WTF. Phone numbers now surface directly in
                every submission card so follow-up is immediate.
              </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-2 xl:w-[360px] xl:grid-cols-1">
              <div className="rounded-[28px] border border-white/10 bg-slate-950/60 p-4">
                <div className="flex items-center gap-3">
                  <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-cyan-400/12 text-cyan-100">
                    <ShieldCheck className="h-5 w-5" />
                  </div>

                  <div>
                    <p className="text-sm font-semibold text-white">
                      {admin.name}
                    </p>
                    <p className="text-sm text-slate-300">{admin.email}</p>
                  </div>
                </div>

                <div className="mt-4 inline-flex rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-300">
                  {admin.role.replace('_', ' ')}
                </div>
              </div>

              <Button
                onClick={() => signOut({ callbackUrl: '/' })}
                variant="outline"
                className="h-auto rounded-[24px] border-white/10 bg-slate-950/60 px-5 py-4 text-sm text-slate-100 transition-transform hover:-translate-y-0.5 hover:border-cyan-300/30 hover:bg-slate-900 hover:text-slate-50"
              >
                <LogOut className="h-4 w-4" />
                Sign out
              </Button>
            </div>
          </div>

          <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            <MetricCard
              className="bg-white/5"
              label="Total submissions"
              value={stats.total}
              description="All builders in the queue"
              toneClassName="text-white"
            />
            <MetricCard
              className="bg-cyan-400/8"
              label="Pending review"
              value={stats.pending}
              description="Needs a human decision"
              toneClassName="text-cyan-100"
            />
            <MetricCard
              className="bg-emerald-400/8"
              label="Approved"
              value={stats.approved}
              description="Ready to welcome in"
              toneClassName="text-emerald-100"
            />
            <MetricCard
              className="bg-rose-400/8"
              label="Rejected"
              value={stats.rejected}
              description="Closed out for now"
              toneClassName="text-rose-100"
            />
          </div>
        </section>

        <section className="rounded-[28px] border border-white/10 bg-slate-950/60 p-4 backdrop-blur-xl sm:p-6">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <p className="text-xs uppercase tracking-[0.28em] text-slate-400">
                Submission inbox
              </p>
              <h2 className="mt-2 text-2xl font-semibold text-white">
                Premium review queue
              </h2>
              <p className="mt-2 text-sm text-slate-300">
                {filteredSubmissions.length} showing
                {deferredSearch ? ` for "${search.trim()}"` : ''}. Pending
                applications stay visually elevated so they are hard to miss.
              </p>
            </div>

            <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
              <div className="relative min-w-[260px] flex-1 sm:min-w-[320px]">
                <Search className="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
                <input
                  value={search}
                  onChange={(event) => setSearch(event.target.value)}
                  placeholder="Search by name, email, phone, or idea..."
                  className="w-full rounded-[22px] border border-white/10 bg-white/5 px-11 py-3 text-sm text-white outline-none transition focus:border-cyan-300/40 focus:bg-white/8 focus:ring-2 focus:ring-cyan-300/20"
                />
              </div>

              <Button
                onClick={refreshSubmissions}
                variant="outline"
                disabled={isRefreshing}
                className="rounded-[22px] border-white/10 bg-white/5 px-4 text-slate-100 hover:border-cyan-300/40 hover:bg-white/10 hover:text-slate-50"
              >
                {isRefreshing ? (
                  <LoaderCircle className="h-4 w-4 animate-spin" />
                ) : (
                  <RefreshCw className="h-4 w-4" />
                )}
                Refresh
              </Button>
            </div>
          </div>

          <div className="mt-5 flex flex-wrap gap-2">
            {filterOptions.map((option) => (
              <button
                key={option.id}
                type="button"
                onClick={() => setFilter(option.id)}
                className={cn(
                  'rounded-full border px-4 py-2 text-sm transition',
                  filter === option.id
                    ? 'border-cyan-300/30 bg-cyan-300/12 text-cyan-50 shadow-[0_12px_30px_-18px_rgba(34,211,238,0.8)]'
                    : 'border-white/10 bg-white/5 text-slate-300 hover:border-white/20 hover:bg-white/8 hover:text-white'
                )}
              >
                {option.label}{' '}
                <span className="text-xs opacity-80">{option.count}</span>
              </button>
            ))}
          </div>
        </section>

        <section className="space-y-5">
          {filteredSubmissions.length === 0 ? (
            <EmptyState hasSearch={Boolean(deferredSearch)} />
          ) : (
            filteredSubmissions.map((submission) => (
              <SubmissionCard
                key={submission.id}
                isUpdating={updatingId === submission.id}
                onDecision={updateSubmissionStatus}
                submission={submission}
              />
            ))
          )}
        </section>
      </main>
    </div>
  );
}

function SubmissionCard({
  submission,
  onDecision,
  isUpdating,
}: {
  submission: AdminSubmission;
  onDecision: (submissionId: number, isApproved: boolean) => Promise<void>;
  isUpdating: boolean;
}) {
  const categories = parseCategories(
    submission.categories,
    submission.otherCategory ?? null
  );
  const status = getStatusTone(submission.isApproved);
  const StatusIcon = status.icon;
  const youtubeEmbedUrl = getYouTubeEmbedUrl(submission.youtubeLink);

  return (
    <article
      className={cn(
        'rounded-[28px] border p-6 backdrop-blur-xl transition duration-300 hover:-translate-y-0.5 hover:border-white/15 sm:p-7 [contain-intrinsic-size:720px] [content-visibility:auto]',
        status.cardClassName
      )}
    >
      <div className="flex flex-col gap-6 xl:flex-row xl:items-start xl:justify-between">
        <div className="space-y-4">
          <div className="flex flex-wrap items-center gap-3">
            <h3 className="text-2xl font-semibold text-white">
              {submission.name}
            </h3>
            <StatusBadge status={submission.isApproved} />
          </div>

          <p className="max-w-2xl text-sm leading-6 text-slate-300">
            Submitted {formatDate(submission.createdAt)} and last touched{' '}
            {formatDate(submission.updatedAt)}.
          </p>

          <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
            <InfoTile
              icon={Mail}
              label="Email"
              value={
                <a
                  className="inline-flex items-center gap-1 text-cyan-100 transition hover:text-white"
                  href={`mailto:${submission.email}`}
                >
                  {submission.email}
                  <ArrowUpRight className="h-3.5 w-3.5" />
                </a>
              }
            />

            <InfoTile
              icon={Phone}
              label="Phone / WhatsApp"
              value={
                submission.whatsapp ? (
                  <a
                    className="inline-flex items-center gap-1 text-cyan-100 transition hover:text-white"
                    href={`tel:${submission.whatsapp}`}
                  >
                    {submission.whatsapp}
                    <ArrowUpRight className="h-3.5 w-3.5" />
                  </a>
                ) : (
                  <span className="text-slate-400">Not shared</span>
                )
              }
            />

            <InfoTile
              icon={StatusIcon}
              label="Review state"
              value={<span className={status.metricClassName}>{status.label}</span>}
            />
          </div>
        </div>

        {submission.isApproved === null && (
          <div className="flex flex-col gap-2 sm:min-w-[220px]">
            <Button
              onClick={() => onDecision(submission.id, true)}
              disabled={isUpdating}
              className="h-11 rounded-2xl bg-emerald-400 text-slate-950 hover:bg-emerald-300"
            >
              {isUpdating ? (
                <LoaderCircle className="h-4 w-4 animate-spin" />
              ) : (
                <CheckCheck className="h-4 w-4" />
              )}
              Approve
            </Button>

            <Button
              onClick={() => onDecision(submission.id, false)}
              disabled={isUpdating}
              variant="outline"
              className="h-11 rounded-2xl border-rose-400/25 bg-rose-400/10 text-rose-50 hover:border-rose-300/35 hover:bg-rose-400/18 hover:text-rose-50"
            >
              {isUpdating ? (
                <LoaderCircle className="h-4 w-4 animate-spin" />
              ) : (
                <XCircle className="h-4 w-4" />
              )}
              Reject
            </Button>
          </div>
        )}
      </div>

      <div className="mt-6 grid gap-4 xl:grid-cols-[0.88fr_1.12fr]">
        <SubmissionSection title="Profile signals">
          <div className="space-y-4">
            <div>
              <p className="text-xs uppercase tracking-[0.22em] text-slate-500">
                Categories
              </p>
              <div className="mt-3 flex flex-wrap gap-2">
                {categories.length > 0 ? (
                  categories.map((category) => (
                    <Badge
                      key={category}
                      variant="outline"
                      className="rounded-full border-white/10 bg-white/5 px-3 py-1 text-slate-100"
                    >
                      {category}
                    </Badge>
                  ))
                ) : (
                  <span className="text-sm text-slate-400">
                    No categories provided.
                  </span>
                )}
              </div>
            </div>

            <div className="rounded-[24px] border border-white/10 bg-white/5 p-4">
              <div className="flex items-start gap-3">
                <div className="mt-0.5 flex h-10 w-10 items-center justify-center rounded-2xl bg-cyan-400/12 text-cyan-100">
                  <Video className="h-4 w-4" />
                </div>
                <div>
                  <p className="text-xs uppercase tracking-[0.22em] text-slate-500">
                    Video reference
                  </p>
                  {youtubeEmbedUrl ? (
                    <div className="mt-3">
                      <div className="aspect-video overflow-hidden rounded-[22px] border border-white/10 bg-slate-950 shadow-[0_24px_60px_-30px_rgba(15,23,42,0.95)]">
                        <iframe
                          src={youtubeEmbedUrl}
                          title={`${submission.name} YouTube reference`}
                          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                          allowFullScreen
                          className="h-full w-full"
                          loading="lazy"
                          referrerPolicy="strict-origin-when-cross-origin"
                        />
                      </div>

                      <a
                        href={submission.youtubeLink}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="mt-3 inline-flex items-center gap-1 text-sm text-cyan-100 transition hover:text-white"
                      >
                        Open on YouTube
                        <ArrowUpRight className="h-3.5 w-3.5" />
                      </a>
                    </div>
                  ) : submission.youtubeLink ? (
                    <a
                      href={submission.youtubeLink}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="mt-2 inline-flex items-center gap-1 text-sm text-cyan-100 transition hover:text-white"
                    >
                      Open YouTube link
                      <ArrowUpRight className="h-3.5 w-3.5" />
                    </a>
                  ) : (
                    <p className="mt-2 text-sm text-slate-400">
                      No video link included.
                    </p>
                  )}
                </div>
              </div>
            </div>

            {submission.interests && (
              <div className="rounded-[24px] border border-white/10 bg-white/5 p-4 text-sm leading-6 text-slate-300">
                <p className="text-xs uppercase tracking-[0.22em] text-slate-500">
                  Legacy interests
                </p>
                <p className="mt-2">{submission.interests}</p>
              </div>
            )}
          </div>
        </SubmissionSection>

        <div className="grid gap-4">
          <SubmissionSection title="WTF idea">
            <p className="text-sm leading-7 text-slate-200">
              {submission.wtfIdea || 'No idea shared yet.'}
            </p>
          </SubmissionSection>

          <SubmissionSection title="Current project">
            <p className="text-sm leading-7 text-slate-200">
              {submission.currentProject || 'No project details shared yet.'}
            </p>
          </SubmissionSection>
        </div>
      </div>
    </article>
  );
}

function MetricCard({
  label,
  value,
  description,
  className,
  toneClassName,
}: {
  label: string;
  value: number;
  description: string;
  className?: string;
  toneClassName?: string;
}) {
  return (
    <div
      className={cn(
        'rounded-[26px] border border-white/10 p-5 backdrop-blur-sm',
        className
      )}
    >
      <p className="text-xs uppercase tracking-[0.22em] text-slate-400">
        {label}
      </p>
      <p className={cn('mt-3 text-3xl font-semibold', toneClassName)}>
        {value}
      </p>
      <p className="mt-2 text-sm text-slate-300">{description}</p>
    </div>
  );
}

function StatusBadge({ status }: { status: boolean | null }) {
  const tone = getStatusTone(status);
  const Icon = tone.icon;

  return (
    <Badge
      variant="outline"
      className={cn('gap-1 rounded-full border px-3 py-1', tone.badgeClassName)}
    >
      <Icon className="h-3.5 w-3.5" />
      {tone.label}
    </Badge>
  );
}

function InfoTile({
  icon: Icon,
  label,
  value,
}: {
  icon: LucideIcon;
  label: string;
  value: ReactNode;
}) {
  return (
    <div className="rounded-[22px] border border-white/10 bg-white/5 p-4">
      <div className="flex items-start gap-3">
        <div className="mt-0.5 flex h-9 w-9 items-center justify-center rounded-2xl bg-white/8 text-slate-200">
          <Icon className="h-4 w-4" />
        </div>
        <div className="min-w-0">
          <p className="text-xs uppercase tracking-[0.22em] text-slate-500">
            {label}
          </p>
          <div className="mt-2 break-words text-sm text-slate-100">{value}</div>
        </div>
      </div>
    </div>
  );
}

function SubmissionSection({
  title,
  children,
}: {
  title: string;
  children: ReactNode;
}) {
  return (
    <section className="rounded-[26px] border border-white/10 bg-white/5 p-5">
      <p className="text-xs uppercase tracking-[0.24em] text-slate-500">
        {title}
      </p>
      <div className="mt-4">{children}</div>
    </section>
  );
}

function EmptyState({ hasSearch }: { hasSearch: boolean }) {
  return (
    <div className="rounded-[28px] border border-dashed border-white/10 bg-slate-950/50 p-10 text-center backdrop-blur-xl">
      <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-3xl bg-white/5 text-slate-200">
        <Search className="h-5 w-5" />
      </div>
      <h3 className="mt-5 text-xl font-semibold text-white">
        {hasSearch ? 'No matching submissions' : 'No submissions yet'}
      </h3>
      <p className="mt-2 text-sm text-slate-300">
        {hasSearch
          ? 'Try a different search term or switch filters to widen the inbox.'
          : 'New applications will appear here as soon as they come in.'}
      </p>
    </div>
  );
}

function getSubmissionStats(submissions: AdminSubmission[]) {
  return submissions.reduce(
    (accumulator, submission) => {
      accumulator.total += 1;

      if (submission.isApproved === null) {
        accumulator.pending += 1;
      } else if (submission.isApproved) {
        accumulator.approved += 1;
      } else {
        accumulator.rejected += 1;
      }

      return accumulator;
    },
    {
      approved: 0,
      pending: 0,
      rejected: 0,
      total: 0,
    }
  );
}

function getStatusTone(status: boolean | null) {
  if (status === true) {
    return statusCopy.approved;
  }

  if (status === false) {
    return statusCopy.rejected;
  }

  return statusCopy.pending;
}

function parseCategories(
  categories: string | undefined,
  otherCategory: string | null
) {
  if (!categories) {
    return [];
  }

  try {
    return (JSON.parse(categories) as string[]).map((category) =>
      category === 'Other' && otherCategory
        ? `Other: ${otherCategory}`
        : category
    );
  } catch (error) {
    console.error('Category parse error:', error);
    return [];
  }
}

function buildSearchBlob(submission: AdminSubmission) {
  return [
    submission.name,
    submission.email,
    submission.whatsapp,
    submission.categories,
    submission.otherCategory,
    submission.wtfIdea,
    submission.currentProject,
    submission.youtubeLink,
    submission.interests,
  ]
    .filter(Boolean)
    .join(' ')
    .toLowerCase();
}

function formatDate(date: string) {
  return dateFormatter.format(new Date(date));
}

function getYouTubeEmbedUrl(url?: string) {
  if (!url) {
    return null;
  }

  try {
    const parsedUrl = new URL(url);
    let videoId: string | null = null;

    if (parsedUrl.hostname === 'youtu.be') {
      videoId = parsedUrl.pathname.split('/').filter(Boolean)[0] ?? null;
    } else if (parsedUrl.hostname.includes('youtube.com')) {
      if (parsedUrl.pathname === '/watch') {
        videoId = parsedUrl.searchParams.get('v');
      } else if (parsedUrl.pathname.startsWith('/shorts/')) {
        videoId = parsedUrl.pathname.split('/')[2] ?? null;
      } else if (parsedUrl.pathname.startsWith('/embed/')) {
        videoId = parsedUrl.pathname.split('/')[2] ?? null;
      }
    }

    if (!videoId) {
      return null;
    }

    const embedUrl = new URL(`https://www.youtube.com/embed/${videoId}`);
    const startAt = parsedUrl.searchParams.get('t');

    if (startAt) {
      const seconds = Number.parseInt(startAt, 10);

      if (!Number.isNaN(seconds) && seconds > 0) {
        embedUrl.searchParams.set('start', String(seconds));
      }
    }

    return embedUrl.toString();
  } catch (error) {
    console.error('YouTube URL parse error:', error);
    return null;
  }
}
