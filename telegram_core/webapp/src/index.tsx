import ReactDOM from 'react-dom/client';
import { StrictMode } from 'react';
import { retrieveLaunchParams } from '@telegram-apps/sdk-react';

import {Root} from "./components/app/Root.tsx";
import {EnvUnsupported} from "./components/unsupported/Unsopported.tsx";
import {init} from "./init.ts";

// Mock the environment in case, we are outside Telegram.
import './mocks.ts';

const root = ReactDOM.createRoot(document.getElementById('react-root')!);

try {
  const launchParams = retrieveLaunchParams();
  const { tgWebAppPlatform: platform } = launchParams;
  const debug = (launchParams.tgWebAppStartParam || '').includes('platformer_debug')
    || import.meta.env.DEV;

  await init({
    debug,
    mockForMacOS: platform === 'macos',
  })
    .then(() => {
      root.render(
        <StrictMode>
          <Root/>
        </StrictMode>,
      );
    });
} catch (err) {
  root.render(<EnvUnsupported/>);
}