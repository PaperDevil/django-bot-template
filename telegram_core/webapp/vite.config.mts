// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import mkcert from 'vite-plugin-mkcert';
import path from 'path';

const BundleLocations = {
  index: "./src/index"
};

export default defineConfig({
  plugins: [
    react({
      plugins: [
        [
          '@swc/plugin-styled-components',
          {
            displayName: true,
            ssr: false,
            fileName: false,
            minify: true,
          },
        ],
      ],
    }),
    process.env.HTTPS && mkcert()
  ],
  resolve: {
    alias: [{ find: "@", replacement: path.resolve(__dirname, "./src") }]
  },
  server: {
    cors: true,
    host: true,
    hmr: {
      protocol: 'ws',
      host: 'localhost',
    },
  },
  build: {
    outDir: '../static/react',
    minify: 'terser',
    target: 'esnext',
    rollupOptions: {
      input: BundleLocations,
      output: {
        entryFileNames: '[name].min.js',
        chunkFileNames: '[name]-[hash].js',
        assetFileNames: '[name][extname]',
      },
    },
  },
  css: {
    modules: {
      localsConvention: 'camelCase',
    },
  },
});
