'use client';

import { type FormEvent, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { signIn } from 'next-auth/react';
import { ArrowLeft, LoaderCircle, Lock, ShieldCheck, Sparkles } from 'lucide-react';
import { toast } from 'sonner';
import { Button } from '@/components/ui/button';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setIsLoading(true);

    try {
      const result = await signIn('credentials', {
        email,
        password,
        redirect: false,
      });

      if (result?.error) {
        toast.error('Invalid credentials. Please try again.');
      } else {
        toast.success('Logged in successfully.');
        router.push('/admin');
        router.refresh();
      }
    } catch (error) {
      console.error('Login error:', error);
      toast.error('Something went wrong. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen overflow-hidden bg-[#07131f] text-slate-50">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.24),_transparent_24%),radial-gradient(circle_at_bottom_right,_rgba(45,212,191,0.18),_transparent_32%),linear-gradient(180deg,_#07131f_0%,_#020617_100%)]" />
        <div className="absolute left-[-6rem] top-16 h-72 w-72 rounded-full bg-cyan-400/12 blur-3xl" />
        <div className="absolute bottom-[-8rem] right-[-3rem] h-80 w-80 rounded-full bg-teal-300/12 blur-3xl" />
        <div className="absolute inset-0 opacity-30 [background-image:linear-gradient(to_right,rgba(148,163,184,0.08)_1px,transparent_1px),linear-gradient(to_bottom,rgba(148,163,184,0.08)_1px,transparent_1px)] [background-size:72px_72px] [mask-image:radial-gradient(circle_at_center,black,transparent_82%)]" />
      </div>

      <main className="relative mx-auto flex min-h-screen max-w-6xl items-center px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid w-full gap-6 lg:grid-cols-[1.08fr_0.92fr]">
          <section className="rounded-[32px] border border-white/10 bg-white/5 p-6 shadow-[0_40px_140px_-48px_rgba(8,47,73,0.95)] backdrop-blur-xl sm:p-8 lg:p-10">
            <Link
              href="/"
              className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200 transition hover:border-cyan-300/30 hover:bg-white/10 hover:text-white"
            >
              <ArrowLeft className="h-4 w-4" />
              Back to home
            </Link>

            <div className="mt-8 inline-flex items-center gap-2 rounded-full border border-cyan-300/20 bg-cyan-300/10 px-3 py-1 text-xs font-medium uppercase tracking-[0.28em] text-cyan-100/90">
              <Sparkles className="h-3.5 w-3.5" />
              Private Admin Portal
            </div>

            <h1 className="mt-5 max-w-2xl font-serif text-4xl leading-tight text-white sm:text-5xl">
              Minimal, premium access for the team behind CWRU.WTF.
            </h1>

            <p className="mt-4 max-w-xl text-sm leading-7 text-slate-300 sm:text-base">
              Reviewer access now matches the new admin dashboard with calmer
              contrast, a tighter layout, and a smoother handoff into the
              moderation queue.
            </p>

            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              <div className="rounded-[26px] border border-white/10 bg-slate-950/55 p-5">
                <p className="text-xs uppercase tracking-[0.22em] text-slate-500">
                  What&apos;s inside
                </p>
                <p className="mt-3 text-lg font-semibold text-white">
                  Submission review
                </p>
                <p className="mt-2 text-sm leading-6 text-slate-300">
                  Cleaner filtering, quick contact details, and a polished
                  moderation surface.
                </p>
              </div>

              <div className="rounded-[26px] border border-white/10 bg-slate-950/55 p-5">
                <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-cyan-400/12 text-cyan-100">
                  <ShieldCheck className="h-5 w-5" />
                </div>
                <p className="mt-4 text-lg font-semibold text-white">
                  Restricted access
                </p>
                <p className="mt-2 text-sm leading-6 text-slate-300">
                  Only approved admins can enter and manage community
                  applications.
                </p>
              </div>
            </div>
          </section>

          <section className="rounded-[32px] border border-white/10 bg-slate-950/70 p-6 backdrop-blur-xl sm:p-8 lg:p-10">
            <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-cyan-400/12 text-cyan-100">
              <Lock className="h-5 w-5" />
            </div>

            <h2 className="mt-6 text-3xl font-semibold text-white">
              Sign in to admin
            </h2>
            <p className="mt-2 text-sm leading-6 text-slate-300">
              Use your admin credentials to open the submission console.
            </p>

            <form onSubmit={handleSubmit} className="mt-8 space-y-4">
              <div>
                <label
                  htmlFor="email"
                  className="mb-2 block text-sm font-medium text-slate-200"
                >
                  Email
                </label>
                <input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                  autoComplete="email"
                  required
                  placeholder="admin@cwru.wtf"
                  className="w-full rounded-[22px] border border-white/10 bg-white/5 px-4 py-3 text-white outline-none transition placeholder:text-slate-500 focus:border-cyan-300/40 focus:bg-white/8 focus:ring-2 focus:ring-cyan-300/20"
                />
              </div>

              <div>
                <label
                  htmlFor="password"
                  className="mb-2 block text-sm font-medium text-slate-200"
                >
                  Password
                </label>
                <input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                  autoComplete="current-password"
                  required
                  placeholder="••••••••"
                  className="w-full rounded-[22px] border border-white/10 bg-white/5 px-4 py-3 text-white outline-none transition placeholder:text-slate-500 focus:border-cyan-300/40 focus:bg-white/8 focus:ring-2 focus:ring-cyan-300/20"
                />
              </div>

              <Button
                type="submit"
                disabled={isLoading}
                className="h-12 w-full rounded-[22px] bg-cyan-300 text-slate-950 hover:bg-cyan-200 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {isLoading ? (
                  <LoaderCircle className="h-4 w-4 animate-spin" />
                ) : (
                  <Lock className="h-4 w-4" />
                )}
                {isLoading ? 'Signing in...' : 'Enter admin dashboard'}
              </Button>
            </form>

            <p className="mt-6 text-sm leading-6 text-slate-400">
              Need an admin account? Contact the current site operator to be
              added to the reviewer list.
            </p>
          </section>
        </div>
      </main>
    </div>
  );
}
