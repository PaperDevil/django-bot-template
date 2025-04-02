import type { ComponentType, JSX } from 'react';

import Index from '../pages/index/index.tsx';

interface Route {
  path: string;
  Component: ComponentType;
  title?: string;
  icon?: JSX.Element;
}

export const routes: Route[] = [
  { path: '/', Component: Index }
];